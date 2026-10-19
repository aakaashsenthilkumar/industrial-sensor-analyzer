from pathlib import Path
import sqlite3

import pandas as pd
from sklearn.ensemble import IsolationForest

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "sensor_readings.db"

FEATURES = ["temperature", "pressure", "vibration"]

def main():
    # 1. connect to the SQLite database.
    connection = sqlite3.connect(DB_PATH)

    try:
        # 2. use sql to retrieve the sensor readings
        query = """
            SELECT timestamp, temperature, pressure, vibration
            FROM sensor_readings
            ORDER BY timestamp
        """

        df = pd.read_sql_query(query, connection)

        if df.empty:
            raise ValueError("No sensor readins found in the database.")

        # 3. select the measurements used by the model
        X = df[FEATURES]

        # 4. create and train the anomaly detection model
        model = IsolationForest(
            n_estimators=100,
            contamination=0.02,
            random_state=42
        )

        prediction = model.fit_predict(X)

        # 5. attach the predictions and scores to the readings
        results = df.copy()
        results["ml_anomaly"] = prediction == -1
        results["anomaly_score"] = -model.score_samples(X)
        results["decision_score"] = model.decision_function(X)
        results["raw_model_score"] = model.score_samples(X)

        # 6. save predictions to a separate sql table
        results.to_sql(
            "ml_anomaly_results",
            connection,
            if_exists="replace",
            index=False,
        )

        # 7. use sql to retrieve the most unusual readings
        anomaly_query = """
            SELECT timestamp, temperature, pressure, vibration, anomaly_score
            FROM ml_anomaly_results
            WHERE ml_anomaly = 1
            ORDER BY anomaly_score DESC
            LIMIT 10
        """

        anomalies = pd.read_sql_query(anomaly_query, connection)

        # load the rule based anomaly report into SQLite
        rules_df = pd.read_csv(
            PROJECT_ROOT / "data" / "detected_anomalies.csv"
        )

        rules_df.to_sql(
            "detected_anomalies",
            connection,
            if_exists="replace",
            index=False,
        )

        # 8. compare ML results with the rule based detector.
        comparison_query = """
            SELECT
                ml.timestamp,
                ml.temperature,
                ml.pressure,
                ml.vibration,
                ml.ml_anomaly,
                ml.anomaly_score,
                ml.decision_score,
                CASE
                    WHEN rules.timestamp IS NOT NULL THEN 1
                    ELSE 0
                END AS rule_anomaly
            FROM ml_anomaly_results as ml
            LEFT JOIN detected_anomalies AS rules
                ON ml.timestamp = rules.timestamp
            ORDER BY ml.timestamp
        """

        comparison = pd.read_sql_query(
            comparison_query, connection
        )

        print(f"Readings analyzed: {len(results)}")
        print(f"Anomalies detected: {int(results['ml_anomaly'].sum())}")
        print("Results saved to SQL table: ml_anomaly_results")
        print("\nMost unusual readings:")
        print(anomalies.to_string(index=False))

        print("\nDetector agreement:")
        print(
            comparison.groupby(
                ["ml_anomaly", "rule_anomaly"]
            ).size()
        )

        print("\nReadings flagged only by rules:")

        rules_only = comparison[
            (comparison["ml_anomaly"] == 0)
            & (comparison["rule_anomaly"] == 1)
        ]

        print(
            rules_only[
                [
                    "timestamp",
                    "temperature",
                    "pressure",
                    "vibration",
                    "anomaly_score",
                    "decision_score",
                ]
            ].to_string(index=False)
        )

        print("\nModel score summary:")
        print(results["raw_model_score"].describe())

        print("\nModel decision function summary:")
        print(model.decision_function(X).min())
        print(model.decision_function(X).max())

    finally:
        # 8. Close the database connection.
        connection.close()


if __name__ == "__main__":
    main()

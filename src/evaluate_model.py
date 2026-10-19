from pathlib import Path
import sqlite3

import pandas as pd
from sklearn.metrics import (
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
)

PROJECT_ROOT = Path(__file__).resolve().parent.parent
DB_PATH = PROJECT_ROOT / "data" / "sensor_readings.db"

def main():
    connection = sqlite3.connect(DB_PATH)

    try:
        query = """
            SELECT timestamp, temperature, pressure, vibration, ml_anomaly
            FROM ml_anomaly_results
            ORDER BY timestamp
        """

        df = pd.read_sql_query(query, connection)

        if df.empty:
            raise ValueError(
                "No ML results found. Run the ML detector first."
            )

        # ground truth: the deliberately injected event.
        event_start = pd.Timestamp("2026-01-01 08:20:00")
        event_end = pd.Timestamp("2026-01-01 09:05:00")

        timestamps = pd.to_datetime(df["timestamp"])

        actual = (
            (timestamps >= event_start)
            & (timestamps <= event_end)
        )

        predicted = df["ml_anomaly"].astype(bool)

        print("\nMissed anomalies:")
        print(df[actual & ~predicted].to_string(index=False))

        print("\nFalse alarms:")
        print(df[~actual & predicted].to_string(index=False))

        print(f"Total readings: {len(df)}")
        print(f"Known synthetic anomalies: {int(actual.sum())}")
        print(f"ML anomalies detected: {int(predicted.sum())}")

        print("\nEvaluation metrics:")
        print(
            f"Precision: "
            f"{precision_score(actual,predicted,zero_division=0):.3f}"
        )
        print(
            f"Recall: "
            f"{recall_score(actual, predicted, zero_division=0):.3f}"
        )
        print(
            f"F1 score: "
            f"{f1_score(actual, predicted, zero_division=0):.3f}"
        )

        tn, fp, fn, tp = confusion_matrix(
            actual, predicted, labels=[False, True]
        ).ravel()

        print("\nConfusion matrix counts:")
        print(f"True negatives: {tn}")
        print(f"False positives: {fp}")
        print(f"False negatives: {fn}")
        print(f"True positives: {tp}")

    finally:
        connection.close()

if __name__ == "__main__":
    main()
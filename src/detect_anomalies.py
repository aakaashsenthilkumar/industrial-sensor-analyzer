import pandas as pd

# load the data
df = pd.read_csv("data/sensor_readings.csv")

# define what counts as normal
df["high_temperature"] = df["temperature"] > 80
df["high_vibration"] = df["vibration"] > 3.0

pressure_mean = df["pressure"].mean()
pressure_std = df["pressure"].std()

df["abnormal_pressure"] = (
    (df["pressure"] < pressure_mean - 3 * pressure_std) |
    (df["pressure"] > pressure_mean + 3 * pressure_std)
)

# flag a reading if any sensor looks abnormal
df["anomaly"] = (
    df["high_temperature"] |
    df["high_vibration"] |
    df["abnormal_pressure"]
)

# explain why each reading was flagged
df["anomaly_reason"] = ""

df.loc[df["high_temperature"], "anomaly_reason"] += "High temperature; "
df.loc[df["high_vibration"], "anomaly_reason"] += "High vibration; "
df.loc[df["abnormal_pressure"], "anomaly_reason"] += "Abnormal pressure; "

# display the flagged readings
anomalies = df[df["anomaly"]]

print("Total readings:", len(df))
print("Suspicious readings:", len(anomalies))

print("\nAnomaly details::")
print(
    anomalies[
        ["timestamp",
        "temperature",
        "pressure",
        "vibration",
        "anomaly_reason",
        ]
    ].to_string(index=True)
)

# save the results
anomalies.to_csv("data/detected_anomalies.csv", index=False)
print("\nSaved anomaly report to data/detected_anomalies.csv")
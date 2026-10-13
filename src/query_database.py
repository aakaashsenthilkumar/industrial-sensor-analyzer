import sqlite3
import pandas as pd

connection = sqlite3.connect("data/sensor_readings.db")

# 1. count the total number of readings
count_query = """
SELECT COUNT(*) AS total_readings
FROM sensor_readings
"""

# 2. Find readings with high temperature or vibration
anomaly_query = """
SELECT timestamp, temperature, pressure, vibration
FROM sensor_readings
WHERE temperature > 80 OR vibration > 3.0
ORDER BY timestamp
"""

total = pd.read_sql_query(count_query, connection)
anomalies = pd.read_sql_query(anomaly_query, connection)

print("Total readings:", total.loc[0, "total_readings"])
print("\nPotential anomalies")
print(anomalies.to_string(index=False))

connection.close()
import sqlite3
import pandas as pd

# load sensor readingsz from the CSV
df = pd.read_csv("data/sensor_readings.csv")

# connect to the database (creates it if it doesn't exist)
connection = sqlite3.connect("data/sensor_readings.db")

# save the DataFrame as a database table
df.to_sql(
    "sensor_readings",
    connection,
    if_exists="replace",
    index=False
)

print("Sensor data loaded into SQLite.")
print("Number of rows:", len(df))

# query the database using SQL
query = """
SELECT timestamp, temperature, vibration
FROM sensor_readings
WHERE temperature > 80
ORDER BY temperature DESC
"""

results = pd.read_sql_query(query,connection)

print("\nHigh-temperature readings:")
print(results.to_string(index=False))

# close the database connection
connection.close()
import pandas as pd

# load the csv
df = pd.read_csv("data/sensor_readings.csv")

print(df.head())

# inspect the dataset
print("\nDataset shape:")
print(df.shape)

print("\nColumn data type:")
print(df.dtypes)

print("\nDataset information:")
print(df.info)

# calculate statistics
print("\nSummary statistics:")
print(df[["temperature","pressure","vibration"]].describe())

# find unusually high temperatures
high_temperature = df[df["temperature"] > 80]

print("\nHigh temperature readings:")
print(high_temperature)

print(f"\nNumber of high temperature readings: {len(high_temperature)}")
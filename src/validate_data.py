from pathlib import Path
import pandas as pd

PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "sensor_readings.csv"

df = pd.read_csv(CSV_PATH)

required_columns = [
    "timestamp",
    "temperature",
    "pressure",
    "vibration",
]

# check 1: required columns must exist
missing_columns = [
    column for column in required_columns
    if column not in df.columns
]

if missing_columns:
    raise ValueError(f"Missing required colums: {missing_columns}")

# check 2: data must not be empty
if df.empty:
    raise ValueError("Sensor data file is empty.")

# check 3: sensor readings must be numeric and present
sensor_columns = ["temperature", "pressure", "vibration"]

for column in sensor_columns:
    df[column] = pd.to_numeric(df[column], errors="coerce")
    
    if df[column].isna().any():
        raise ValueError(
            f"Column '{column}' contains missing or non-numeric values."
        )

# check 4: timestamps must be valid
df["timestamp"] = pd.to_datetime(
    df["timestamp"],
    errors="coerce",
)

if df["timestamp"].isna().any():
    raise ValueError("One or more timestamps are invalid")

# check 5: timestamps must not be duplicate
if df["timestamp"].duplicated().any():
    raise ValueError("Duplicate timestamps detected")

# check 6: readings must be within plausible ranges
plausible_ranges = {
    "temperature": (-50,200),
    "pressure": (0,500),
    "vibration": (0,100),
}

for column, (minimum, maximum) in plausible_ranges.items():
    invalid = ~df[column].between(minimum, maximum)

    if invalid.any():
        raise ValueError(
            f"Column '{column}' has values outside "
            f"the allowed range {minimum} to {maximum}."
        )

# check 7: timestamps should be chronological
if not df["timestamp"].is_monotonic_increasing:
    raise ValueError("Timestamps are not in chronological order.")

print(f"Data validation passed: {len(df)} rows checked.")
print("All required columns, readings, and timestamps passed.")
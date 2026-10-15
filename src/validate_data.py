
from pathlib import Path

import pandas as pd


PROJECT_ROOT = Path(__file__).resolve().parent.parent
CSV_PATH = PROJECT_ROOT / "data" / "sensor_readings.csv"

REQUIRED_COLUMNS = [
    "timestamp",
    "temperature",
    "pressure",
    "vibration",
]

PLAUSIBLE_RANGES = {
    "temperature": (-50, 200),
    "pressure": (0, 500),
    "vibration": (0, 100),
}


def validate_data(df: pd.DataFrame) -> pd.DataFrame:
    """Validate sensor data and return a cleaned copy."""

    # Work on a copy so the original DataFrame stays unchanged.
    df = df.copy()

    # Check 1: Required columns must exist.
    missing_columns = [
        column for column in REQUIRED_COLUMNS
        if column not in df.columns
    ]

    if missing_columns:
        raise ValueError(
            f"Missing required columns: {missing_columns}"
        )

    # Check 2: Data must not be empty.
    if df.empty:
        raise ValueError("Sensor data file is empty.")

    # Check 3: Sensor readings must be numeric and present.
    for column in PLAUSIBLE_RANGES:
        df[column] = pd.to_numeric(
            df[column],
            errors="coerce",
        )

        if df[column].isna().any():
            raise ValueError(
                f"Column '{column}' contains missing "
                "or non-numeric values."
            )

    # Check 4: Timestamps must be valid.
    df["timestamp"] = pd.to_datetime(
        df["timestamp"],
        format="mixed",
        errors="coerce",
    )

    if df["timestamp"].isna().any():
        raise ValueError("One or more timestamps are invalid.")

    # Check 5: Timestamps must not be duplicated.
    if df["timestamp"].duplicated().any():
        raise ValueError("Duplicate timestamps detected.")

    # Check 6: Readings must be within plausible ranges.
    for column, (minimum, maximum) in PLAUSIBLE_RANGES.items():
        invalid = ~df[column].between(minimum, maximum)

        if invalid.any():
            raise ValueError(
                f"Column '{column}' has values outside "
                f"the allowed range {minimum} to {maximum}."
            )

    # Check 7: Timestamps must be chronological.
    if not df["timestamp"].is_monotonic_increasing:
        raise ValueError("Timestamps are not in chronological order.")

    return df


def main() -> None:
    """Load the CSV, validate it, and report the result."""

    df = pd.read_csv(CSV_PATH)
    validated_df = validate_data(df)

    print(f"Data validation passed: {len(validated_df)} rows checked.")
    print("All required columns, readings, and timestamps passed.")


if __name__ == "__main__":
    main()
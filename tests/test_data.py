
import pandas as pd
import pytest

from src.validate_data import validate_data


def make_valid_data():
    """Create a small, valid sensor dataset for testing."""

    return pd.DataFrame({
        "timestamp": [
            "2026-01-01 00:00:00",
            "2026-01-01 00:05:00",
        ],
        "temperature": [70.0, 72.0],
        "pressure": [100.0, 102.0],
        "vibration": [2.0, 2.2],
    })


def test_sensor_data_has_expected_columns():
    df = pd.read_csv("data/sensor_readings.csv")

    expected_columns = {
        "timestamp",
        "temperature",
        "pressure",
        "vibration",
    }

    assert expected_columns.issubset(df.columns)


def test_sensor_data_has_500_rows():
    df = pd.read_csv("data/sensor_readings.csv")

    assert len(df) == 500


def test_sensor_readings_are_numeric():
    df = pd.read_csv("data/sensor_readings.csv")

    for column in ["temperature", "pressure", "vibration"]:
        assert pd.api.types.is_numeric_dtype(df[column])


def test_valid_data_passes_validation():
    df = make_valid_data()

    result = validate_data(df)

    assert len(result) == 2
    assert pd.api.types.is_datetime64_any_dtype(result["timestamp"])


def test_missing_column_is_rejected():
    df = make_valid_data().drop(columns=["pressure"])

    with pytest.raises(ValueError, match="Missing required columns"):
        validate_data(df)


def test_empty_data_is_rejected():
    df = make_valid_data().iloc[0:0]

    with pytest.raises(ValueError, match="empty"):
        validate_data(df)



def test_non_numeric_sensor_reading_is_rejected():
    df = make_valid_data()

    # Convert the column to a type that can hold text.
    df["temperature"] = df["temperature"].astype(object)

    # Insert an invalid sensor reading.
    df.loc[0, "temperature"] = "not a number"

    with pytest.raises(ValueError, match="non-numeric"):
        validate_data(df)


def test_invalid_timestamp_is_rejected():
    df = make_valid_data()
    df.loc[0, "timestamp"] = "not a timestamp"

    with pytest.raises(ValueError, match="timestamps are invalid"):
        validate_data(df)


def test_duplicate_timestamp_is_rejected():
    df = make_valid_data()
    df.loc[1, "timestamp"] = df.loc[0, "timestamp"]

    with pytest.raises(ValueError, match="Duplicate timestamps"):
        validate_data(df)


def test_out_of_range_temperature_is_rejected():
    df = make_valid_data()
    df.loc[0, "temperature"] = 250

    with pytest.raises(ValueError, match="outside"):
        validate_data(df)


def test_out_of_order_timestamps_are_rejected():
    df = make_valid_data()
    df.loc[1, "timestamp"] = "2025-12-31 23:55:00"

    with pytest.raises(ValueError, match="chronological order"):
        validate_data(df)
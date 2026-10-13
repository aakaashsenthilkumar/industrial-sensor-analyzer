import pandas as pd

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
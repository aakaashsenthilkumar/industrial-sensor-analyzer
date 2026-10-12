# Industrial Sensor Analyzer

A Python-based project that generates simulated industrial sensor readings, analyzes sensor data, visualizes trends, and flags potentially abnormal readings.

## Features

- Generates simulated temperature, pressure, and vibration readings.
- Analyzes datasets using pandas.
- Plots sensor readings over time using Matplotlib.
- Flags suspicious readings using rule-based thresholds and statistical pressure limits.
- Exports detected anomalies to a CSV report.

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- scikit-learn (planned for the machine learning extension)

## Project Structure

- `src/data_generator.py` — generates simulated sensor data.
- `src/analyze.py` — explores the dataset and calculates summary statistics.
- `src/plot_sensors.py` — creates sensor trend plots.
- `src/detect_anomalies.py` — detects and exports suspicious readings.
- `data/` — stores generated readings, plots, and anomaly reports.

## How to Run

Create and activate a Python virtual environment, then install the required dependencies.

Run these commands from the project root:

```bash
python src/data_generator.py
python src/analyze.py
python src/plot_sensors.py
python src/detect_anomalies.py
```

## Current Limitations

The data is simulated rather than collected from real equipment. Detection rules are experimental and are not validated for real industrial safety or maintenance decisions.

## Planned Improvements

- Train and evaluate a machine learning anomaly detection model.
- Add automated tests.
- Compare rule-based and machine learning results.
- Add SQL storage and queries.

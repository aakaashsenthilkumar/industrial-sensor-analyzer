# Industrial Sensor Analyzer

A Python-based data analysis pipeline for simulated industrial sensor readings. The project validates sensor data, generates visualizations, identifies potential anomalies, and stores readings in SQLite for SQL-based analysis.

## Features

- **Data generation:** Creates simulated temperature, pressure, and vibration readings.
- **Data validation:** Checks required columns, numeric values, timestamps, duplicate readings, chronological order, and configurable plausibility ranges.
- **Data analysis:** Uses pandas to inspect readings and calculate descriptive statistics.
- **Visualization:** Generates time-series plots for sensor measurements.
- **Anomaly detection:** Flags potential anomalies using configurable thresholds and statistical rules.
- **SQL integration:** Stores sensor readings in SQLite and queries the database for potentially abnormal readings.
- **Automated tests:** Tests core data assumptions using pytest.

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- SQLite
- pytest
- Git and GitHub

## Project Structure

```text
industrial-sensor-analyzer/
├── data/
│   ├── sensor_readings.csv
│   ├── sensor_plots.png
│   ├── detected_anomalies.csv
│   └── sensor_readings.db
├── src/
│   ├── data_generator.py
│   ├── validate_data.py
│   ├── analyze.py
│   ├── plot_sensors.py
│   ├── detect_anomalies.py
│   ├── load_database.py
│   ├── query_database.py
│   └── run_pipeline.py
├── tests/
│   └── test_data.py
├── .gitignore
└── README.md
```

## Setup

Requires Python 3.13 or another compatible Python version.

1. Clone the repository and navigate to the project folder.
2. Create and activate a virtual environment.
3. Install the required dependencies.
4. Run the pipeline.

Example commands for Windows PowerShell:

```powershell
git clone https://github.com/aakaashsenthilkumar/industrial-sensor-analyzer.git
cd industrial-sensor-analyzer

python -m venv .venv
.\.venv\Scripts\Activate.ps1

python -m pip install pandas numpy matplotlib pytest
python src/run_pipeline.py
```

## Run Tests

```powershell
python -m pytest
```

## Output

The pipeline generates or updates:

- `data/sensor_readings.csv` — simulated sensor measurements.
- `data/sensor_plots.png` — time-series plots.
- `data/detected_anomalies.csv` — readings flagged by the anomaly detector.
- `data/sensor_readings.db` — SQLite database containing sensor readings.

## Limitations

- Sensor readings are simulated and do not represent a validated real-world equipment dataset.
- Anomaly detection currently uses rule-based thresholds and statistical checks, not a trained machine-learning model.
- Plausibility ranges are demonstration settings, not equipment-specific operating limits.
- A flagged reading is a potential anomaly, not proof of equipment failure.

## Planned Improvements

- Train and evaluate a machine-learning anomaly detection model.
- Compare model-based detection with rule-based detection.
- Build an AI assistant that explains sensor anomalies using technical documentation.
- Expose the analysis through an API and deploy the application.

## Disclaimer

This project is for educational and demonstration purposes. It is not intended for safety-critical decisions or direct control of industrial equipment.
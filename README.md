# Industrial Sensor Analyzer

A Python-based sensor data analysis pipeline built around simulated industrial equipment readings. The project demonstrates data validation, exploratory data analysis, rule-based anomaly detection, visualization, and SQL-based data storage.

## Features

- **Data generation:** Generate a sample dataset containing temperature, pressure, and vibration readings.
- **Data validation:** Check required columns, missing or non-numeric readings, invalid or duplicate timestamps, chronological order, and plausible sensor ranges.
- **Exploratory data analysis:** Summarize sensor readings and identify values that exceed selected thresholds.
- **Anomaly detection:** Flag suspicious readings using configurable rules and statistical thresholds.
- **Data visualization:** Generate plots to help inspect sensor behavior.
- **SQLite integration:** Store readings in a local database and query them using SQL.
- **Automated testing:** Use pytest to test dataset properties and data validation behavior.
- **Pipeline automation:** Run the main project steps sequentially with a single command.

## Tech Stack

- Python
- pandas
- NumPy
- Matplotlib
- SQLite
- pytest

## Project Structure

```text
industrial-sensor-analyzer/
├── data/                 # Generated data, plots, and local database
├── src/
│   ├── data_generator.py
│   ├── validate_data.py
│   ├── analyze.py
│   ├── plot_sensors.py
│   ├── detect_anomalies.py
│   ├── load_database.py
│   ├── query_database.py
│   └── run_pipeline.py
└── tests/
    └── test_data.py
```

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/aakaashsenthilkumar/industrial-sensor-analyzer.git
cd industrial-sensor-analyzer
```

### 2. Create and activate a virtual environment

Windows PowerShell:

```powershell
python -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install pandas numpy matplotlib pytest
```

### 4. Run the pipeline

```powershell
python src/run_pipeline.py
```

The pipeline generates or loads sensor readings, validates the data, performs analysis, creates visualizations, detects anomalies, and loads readings into SQLite for querying.

### 5. Run the tests

```powershell
python -m pytest -v
```

The test suite currently contains 11 tests covering dataset properties and data validation, including invalid readings, timestamps, and out-of-range values.

## Notes

- The sensor dataset is simulated and is intended for learning and software development.
- Validation ranges and anomaly thresholds are configurable examples, not verified operating limits for real industrial equipment.
- Generated datasets, plots, and local database files are kept out of version control.

## Future Improvements

- Add machine-learning-based anomaly detection.
- Evaluate model performance against labeled or synthetic fault conditions.
- Expose analysis through an API.
- Integrate an AI assistant to explain suspicious sensor readings.
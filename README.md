# Industrial Sensor Analyzer

A Python-based predictive maintenance project that analyzes industrial sensor readings, detects anomalies using rule-based logic and machine learning, and stores results in SQLite for SQL-based analysis.

## Features

- **Data validation:** Checks sensor data for missing values, invalid timestamps, duplicates, and unexpected readings.
- **Exploratory data analysis:** Calculates sensor statistics and generates visualizations for temperature, pressure, and vibration.
- **Rule-based anomaly detection:** Flags readings that exceed configured thresholds.
- **Machine learning:** Uses Scikit-learn's Isolation Forest algorithm to identify unusual combinations of sensor measurements.
- **SQL integration:** Stores sensor readings and anomaly results in SQLite for querying and comparison.
- **Model evaluation:** Measures precision, recall, F1 score, and confusion matrix counts against a known synthetic anomaly event.
- **Automated pipeline:** Runs the main data-processing and analysis steps through a single script.
- **Automated testing:** Uses pytest to verify data quality and expected behavior.

## Tech Stack

- **Language:** Python
- **Data processing:** pandas, NumPy
- **Visualization:** Matplotlib
- **Machine learning:** Scikit-learn
- **Database:** SQLite and SQL
- **Testing:** pytest
- **Version control:** Git and GitHub

## Dataset

The project uses 500 synthetic industrial sensor readings.

| Column | Description |
|---|---|
| `timestamp` | Timestamp of each sensor reading |
| `temperature` | Simulated equipment temperature |
| `pressure` | Simulated operating pressure |
| `vibration` | Simulated equipment vibration |

A synthetic anomaly event was deliberately introduced into the dataset to test the detection and evaluation workflow.

**Note:** The dataset is simulated and does not represent measurements from real industrial equipment.

## Project Structure

```text
industrial-sensor-analyzer/
├── data/
│   ├── sensor_readings.csv
│   ├── detected_anomalies.csv
│   ├── sensor_plots.png
│   └── sensor_readings.db
├── src/
│   ├── data_generator.py
│   ├── analyze.py
│   ├── plot_sensors.py
│   ├── detect_anomalies.py
│   ├── load_database.py
│   ├── query_database.py
│   ├── run_pipeline.py
│   ├── validate_data.py
│   ├── ml_detect_anomalies.py
│   └── evaluate_model.py
├── tests/
│   └── test_data.py
├── .gitignore
├── README.md
└── requirements.txt
```

## Getting Started

### 1. Clone the repository

```powershell
git clone https://github.com/aakaashsenthilkumar/industrial-sensor-analyzer.git
cd industrial-sensor-analyzer
```

### 2. Create a virtual environment

```powershell
python -m venv .venv
```

Activate it on Windows PowerShell:

```powershell
.\.venv\Scripts\Activate.ps1
```

### 3. Install dependencies

```powershell
python -m pip install -r requirements.txt
```

## Running the Project

### Run the analysis pipeline

```powershell
python src/run_pipeline.py
```

This runs the main data-processing workflow, including validation, sensor analysis, visualization, rule-based anomaly detection, database loading, and SQL queries.

### Run machine learning anomaly detection

```powershell
python src/ml_detect_anomalies.py
```

The script uses Isolation Forest to identify unusual sensor readings and saves the results to the `ml_anomaly_results` table in SQLite.

### Evaluate the model

```powershell
python src/evaluate_model.py
```

The evaluation script compares model predictions against the deliberately injected synthetic anomaly event and reports precision, recall, F1 score, and confusion matrix counts.

### Run automated tests

```powershell
python -m pytest
```

## Model Evaluation

Using the known synthetic event window as the reference labels, the Isolation Forest model achieved the following results in the current experiment:

| Metric | Result |
|---|---:|
| Precision | 0.900 |
| Recall | 0.900 |
| F1 score | 0.900 |
| True positives | 9 |
| False positives | 1 |
| True negatives | 489 |
| False negatives | 1 |

These results show how well the model detected the injected synthetic event in this dataset. They **do not establish performance on real industrial equipment or real equipment failures**.

## Key Learnings

- Building a structured data-analysis pipeline in Python.
- Validating sensor data before analysis.
- Using pandas and NumPy to process numerical data.
- Querying sensor data with SQL and SQLite.
- Comparing rule-based anomaly detection with unsupervised machine learning.
- Evaluating predictions using precision, recall, F1 score, and a confusion matrix.
- Investigating false positives and false negatives.
- Organizing a Python project with reusable modules, automated tests, and Git version control.

## Future Improvements

- Test detection methods on additional synthetic anomaly scenarios.
- Explore time-series features and alternative anomaly detection algorithms.
- Add integration tests for the complete pipeline.
- Expose sensor analysis and anomaly results through a REST API.
- Extend the project into a predictive maintenance application.
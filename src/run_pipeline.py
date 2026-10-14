from pathlib import Path
import subprocess
import sys

# find the main project folder
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# scripts to run in order
SCRIPTS = [
    "data_generator.py",
    "analyze.py",
    "plot_sensors.py",
    "detect_anomalies.py",
    "load_database.py",
    "query_database.py",
]

# run each script
for script in SCRIPTS:
    script_path = PROJECT_ROOT / "src" / script

    print(f"\n---Running {script} ---", flush=True)

    subprocess.run(
        [sys.executable, str(script_path)],
        cwd=PROJECT_ROOT,
        check=True
    )

print("\nPipeline completed successfully!")
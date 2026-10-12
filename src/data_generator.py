# import the tools we need
import csv
import random
from datetime import datetime, timedelta

# make the random data repeatable
random.seed(42)

# create a function to generate readings
def generate_sensor_data(num_readings=500):
    start_time = datetime(2026,1,1,0,0)
    readings = []

    # generate each timestamp and sensor reading
    for i in range(num_readings):
        timestamp = start_time + timedelta(minutes=5 * i)

        temperature = random.gauss(70,3)
        pressure = random.gauss(150,5)
        vibration = random.gauss(2.0, 0.3)

        # simulate a problem
        if 100 <= i < 110:
            temperature += 20
            vibration += 1.5

        # store each reading in a dictionary
        readings.append({
            "timestamp": timestamp.isoformat(),
            "temperature": round(temperature, 2),
            "pressure": round(pressure, 2),
            "vibration": round(vibration, 3),
        })

    return readings

# save the data to a csv file
def save_to_csv(readings, filename="data/sensor_readings.csv"):
    fieldnames = ["timestamp", "temperature", "pressure", "vibration"]

    with open(filename, "w", newline="", encoding="utf-8") as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(readings)

# tell python what to do when you run the file
if __name__ == "__main__":
    data = generate_sensor_data()
    save_to_csv(data)

    print(f"Generated {len(data)} sensor readings.")
    print("Saved to data/sensor_readings.csv")
    print("\nFirst 3 readings:")

    for reading in data[:3]:
        print(reading)
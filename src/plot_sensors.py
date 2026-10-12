import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# load the sensor readings
df = pd.read_csv("data/sensor_readings.csv")

# convert the timestamp column into actual dates and times
df["timestamp"] = pd.to_datetime(df["timestamp"])

# create a figure with three plots
fig, axes = plt.subplots(3, 1, figsize=(12,8))

# plot temperature
axes[0].plot(df["timestamp"], df["temperature"])
axes[0].set_title("Temperature Over Time")
axes[0].set_ylabel("Temperature")

# plot pressure
axes[1].plot(df["timestamp"], df["pressure"])
axes[1].set_title("Pressure Over Time")
axes[1].set_ylabel("Pressure")

# plot vibration
axes[2].plot(df["timestamp"], df["vibration"])
axes[2].set_title("Vibration Over Time")
axes[2].set_ylabel("Vibration")
axes[2].set_xlabel("Time")

# make the plots fit neatly
plt.tight_layout()

# save the plots as images
plt.savefig("data/sensor_plots.png", dpi=150)
print("Plots saved to data/sensor_plots.png")
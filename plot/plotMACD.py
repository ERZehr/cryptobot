import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime
import pandas as pd

# Read the data from the file and create a DataFrame
data_file = "../data_files/BTC_MACD_last_26_hours"  # Replace with the actual file path
df = pd.read_csv(data_file, names=["Date", "Time", "Value"], parse_dates=["Date", "Time"])

# Combine the Date and Time columns to create a single datetime column
df["Datetime"] = df["Date"] + pd.to_timedelta(df["Time"])

# Set the Datetime column as the index
df.set_index("Datetime", inplace=True)

# Plot the continuous graph
plt.figure(figsize=(10, 6))
plt.plot(df["Value"], marker="o", linestyle="-", color="b")
plt.xlabel("Time")
plt.ylabel("Value")
plt.title("Continuous Graph of Data")
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter("%Y-%m-%d %H:%M:%S"))
plt.gca().xaxis.set_major_locator(mdates.HourLocator(interval=1))  # Display tick every hour
plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

# Show the plot
plt.show()
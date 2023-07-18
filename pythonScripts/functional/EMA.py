#!/usr/bin/python3

import sys
import os
import subprocess

ASSET = sys.argv[1]  # Cryptocurrency
CURRENCY = sys.argv[2]  # Reference currency (Typically USD)
PERIOD = int(sys.argv[3])  # Moving average period
LIMIT = int(sys.argv[4])  # Desired number of data points
RANGE = sys.argv[5]  # Day, hour, minute

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, str(LIMIT), RANGE])  # Run getData.sh to create a data file

FILENAME = ASSET + "_last_" + str(LIMIT) + "_" + RANGE + "s"  # Create a filename
data_file_path = os.path.join("..", "..", "data_files", FILENAME)  # Create the file path

data = []  # List to store the price data
moving_averages = []  # List to store the moving averages
dates = []  # List to store the dates
times = []  # List to store the times

# Read the data from the file and extract the prices, dates, and times
with open(data_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        datetime = parts[0].split(' ')  # Splitting the date and time
        date = datetime[0]
        time = datetime[1]
        price = float(parts[1])  # Extract the price from the line
        data.append(price)  # Add the price to the data list
        dates.append(date)  # Add the date to the dates list
        times.append(time)  # Add the time to the times list

# Calculate the exponential moving averages
alpha = 2 / (PERIOD + 1)  # Smoothing factor
ema = data[0]  # Initial EMA value
moving_averages.append(ema)  # Set the first value into the list

for i in range(1, len(data)):
    ema = alpha * data[i] + (1 - alpha) * ema  # Calculate the EMA
    moving_averages.append(round(ema, 2))  # Add the EMA to the moving_averages list

FILENAME2 = ASSET + "_" + str(PERIOD) + "_" + RANGE + "_EMA_against_last_" + str(LIMIT) + "_" + RANGE + "s" # create filename

with open(FILENAME2, 'w') as file:
    for i, average in enumerate(moving_averages, start=0):
        file.write(f"{dates[i]}, {times[i]}, {average}\n")

os.environ["FILENAME"] = FILENAME  # Set the value of FILENAME2 as an environment variable
subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
print(FILENAME2)  # Print the name of the new file
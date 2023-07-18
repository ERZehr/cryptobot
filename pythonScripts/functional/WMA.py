#!/usr/bin/python3

import sys
import os
import subprocess

ASSET = sys.argv[1]  # cryptocurrency
CURRENCY = sys.argv[2]  # ref currency (Typically USD)
PERIOD = int(sys.argv[3])  # moving average period
LIMIT = int(sys.argv[4])  # desired number of datum
RANGE = sys.argv[5]  # day, hour, minute

DATAQUERY = str(PERIOD + LIMIT - 1)  # number of datum to query

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, DATAQUERY, RANGE])

FILENAME = ASSET + "_last_" + DATAQUERY + "_" + RANGE + "s"
data_file_path = os.path.join("..", "..", "data_files", FILENAME)

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

# Calculate the moving averages
weights = list(range(1, PERIOD + 1))  # Weights for the weighted moving average
weights_sum = sum(weights)  # Sum of the weights
for i in range(len(data) + 1 - PERIOD):  # edited so we don't have an extra false point
    window = data[i:i + PERIOD]  # Extract the window of prices for the current period
    weighted_average = sum([price * weight for price, weight in zip(window, weights)]) / weights_sum  # Calculate the weighted average
    moving_averages.append(round(weighted_average, 2))  # Add the average to the moving_averages list

FILENAME2 = ASSET + "_" + str(PERIOD) + "_" + RANGE + "_period_WMA_against_last_" + str(LIMIT) + "_" + RANGE + "s"

with open(FILENAME2, 'w') as file:
    for i, average in enumerate(moving_averages, start=0):
        file.write(f"{dates[i]}, {times[i]}, {average}\n")

os.environ["FILENAME"] = FILENAME  # Set the value of FILENAME as an environment variable
subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])
print(FILENAME2)
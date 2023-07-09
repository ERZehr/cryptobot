#!/usr/bin/python3

import sys
import os
import subprocess

ASSET = sys.argv[1]  # Cryptocurrency
CURRENCY = sys.argv[2]  # Reference currency (Typically USD)
PERIOD = int(sys.argv[3])  # Moving average period
LIMIT = int(sys.argv[4])  # Desired number of data points

while PERIOD >= LIMIT:
    print("The data window must be longer than the period.")
    PERIOD = int(input("Enter the period: "))
    LIMIT = int(input("Enter the number of desired data points: "))

RANGE = sys.argv[5]  # Day, hour, minute

DATAQUERY = str(PERIOD + LIMIT)  # Number of data points to query

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, DATAQUERY, RANGE])  # Run getData.sh to create a data file

FILENAME = ASSET + "_last_" + DATAQUERY + "_" + RANGE + "s"  # Create a filename
data_file_path = os.path.join("..", "..", "data_files", FILENAME)  # Create the file path

data = []  # List to store the price data
moving_averages = []  # List to store the moving averages

# Read the data from the file and extract the prices
with open(data_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        price = float(parts[1])  # Extract the price from the line
        data.append(price)  # Add the price to the data list

# Calculate the exponential moving averages
alpha = 2 / (PERIOD + 1)  # Smoothing factor
ema = data[0]  # Initial EMA value

for i in range(1, len(data)):
    ema = alpha * data[i] + (1 - alpha) * ema  # Calculate the EMA
    moving_averages.append(round(ema, 2))  # Add the EMA to the moving_averages list

FILENAME2 = ASSET + "_last_" + DATAQUERY + "_" + RANGE + "s_EMA"  # Create a filename

with open(FILENAME2, 'w') as file:  # Write the exponential moving averages to a file
    file.write("Exponential Moving Averages:\n")
    for i, average in enumerate(moving_averages, start=0):
        file.write(f"Period {i}: {average}\n")

os.environ["FILENAME"] = FILENAME  # Set the value of FILENAME2 as an environment variable
subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
print(FILENAME2)  # Print the name of the new file
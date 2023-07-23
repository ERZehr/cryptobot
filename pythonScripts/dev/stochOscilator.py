#!/usr/bin/python3

import sys
import os
import subprocess

ASSET = sys.argv[1]  # Cryptocurrency
CURRENCY = sys.argv[2]  # Reference currency (Typically USD)
LIMIT = int(sys.argv[3])  # Desired number of data points
RANGE = sys.argv[4]  # Day, hour, minute

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, str(int(LIMIT) + 14), RANGE])  # Run getData.sh to create a data file

FILENAME = ASSET + "_last_" + str(int(LIMIT) + 14) + "_" + RANGE + "s"  # Create a filename
data_file_path = os.path.join("..", "..", "data_files", FILENAME)  # Create the file path

with open(data_file_path, "r") as file:
    data = file.readlines()

total_data_points = len(data)
LIMIT = min(LIMIT, total_data_points - 14)  # Adjust LIMIT if it exceeds the available data points

period = 14
highs = [float(row.split(", ")[1]) for row in data]
stochastic_oscillators = []

for i in range(period - 1, period - 1 + LIMIT):
    lowest_low = min(highs[i - period + 1 : i + 1])
    highest_high = max(highs[i - period + 1 : i + 1])
    current_close = highs[i]

    stochastic_oscillator = ((current_close - lowest_low) / (highest_high - lowest_low)) * 100
    stochastic_oscillators.append(stochastic_oscillator)

FILENAME2 = ASSET + "_stochastic_oscillator_last_" + str(LIMIT) + "_" + RANGE + "s" # create filename

with open(FILENAME2, 'w') as file:
    for i, oscillator in enumerate(stochastic_oscillators, start=period):
        file.write(f"{data[i].split(', ')[0]}, {data[i].split(', ')[1].strip()}, {oscillator}\n")

os.environ["FILENAME"] = FILENAME  # Set the value of FILENAME as an environment variable
#subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
print(FILENAME2)  # Print the name of the new file
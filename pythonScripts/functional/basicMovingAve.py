#!/usr/bin/python3

import sys # for inputs
import os # for filepath
import subprocess # for subprocess

ASSET = sys.argv[1] #cryptocurrency
CURRENCY = sys.argv[2] #ref currency (Typically USD)
PERIOD = int(sys.argv[3]) # moving average period
LIMIT = int(sys.argv[4]) # desired number of datum
while (PERIOD >= LIMIT):
    print("The data window must be longer than the period.")
    PERIOD = int(input("Enter the period: "))
    LIMIT = int(input("Enter the number of desired data points: "))

RANGE = sys.argv[5] # day, hour, minute

DATAQUERY = str(PERIOD + LIMIT) # number of datum to query

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, DATAQUERY, RANGE]) # run getData.sh to create a data file

FILENAME = ASSET + "_last_" + DATAQUERY + "_" + RANGE +"s" # create a filename
data_file_path = os.path.join("..", "..", "data_files", FILENAME) # Create the file path

data = []  # List to store the price data
moving_averages = []  # List to store the moving averages

# Read the data from the file and extract the prices
with open(data_file_path, 'r') as file:
    for line in file:
        parts = line.strip().split(', ')
        price = float(parts[1])  # Extract the price from the line
        data.append(price)  # Add the price to the data list

# Calculate the moving averages
for i in range(len(data) - PERIOD): # edited so we dont have an extra false point
    window = data[i:i+PERIOD]  # Extract the window of prices for the current period
    average = sum(window) / PERIOD  # Calculate the average of the window
    moving_averages.append(average)  # Add the average to the moving_averages list

FILENAME2 = ASSET + "_last_" + DATAQUERY + "_" + RANGE +"s_basicMA" # create a filename

with open(FILENAME2, 'w') as file: # write it all to a file
    file.write("Moving Averages:\n")
    for i, average in enumerate(moving_averages, start=0):
        file.write(f"Period {i}: {average}\n")

os.environ["FILENAME"] = FILENAME  # Set the value of FILENAME as an environment variable
subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
print(FILENAME2) # give the name of the new file back to bash
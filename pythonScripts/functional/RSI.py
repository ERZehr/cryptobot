#!/usr/bin/env python3

import sys
import os
import subprocess

DEFPERIOD = 14  # default period is two weeks

ASSET = sys.argv[1]  # set the input args
CURRENCY = sys.argv[2]
LIMIT = sys.argv[3]  # number of days of RSI
RANGE = sys.argv[4]  # minutes days hours
PERIOD = sys.argv[5] if len(sys.argv) >= 6 else str(DEFPERIOD)  # Changed the condition and converted PERIOD to a string

QUERYLENGTH = str(int(LIMIT) + int(PERIOD))

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, QUERYLENGTH, RANGE])

FILENAME = ASSET + "_last_" + QUERYLENGTH + "_" + RANGE + "s"
data_file_path = os.path.join("..", "..", "data_files", FILENAME)

# Read the file contents
with open(data_file_path, "r") as file:
    lines = file.readlines()

price_list = []  # List to store the prices
date_list = []  # List to store the dates
time_list = []  # List to store the times

# Extract the prices, dates, and times from each line
for line in lines:
    parts = line.split(", ")
    datetime = parts[0].split(" ")  # Splitting the date and time
    date = datetime[0]
    time = datetime[1]
    price = float(parts[1])
    date_list.append(date)  # Store the date in date_list
    time_list.append(time)  # Store the time in time_list
    price_list.append(price)  # Store the price in price_list

n = len(price_list)
gains = []  # List for gains
losses = []  # List for losses

# Calculate gains and losses
for i in range(1, n):
    price_diff = price_list[i] - price_list[i - 1]
    if price_diff > 0:
        gains.append(price_diff)
        losses.append(0)
    else:
        gains.append(0)
        losses.append(price_diff)

n = len(gains)
gain_ave = []  # List for gain averages
loss_ave = []  # List for loss averages

# Calculate gain and loss averages
for i in range(n - int(PERIOD) + 1):
    gain = sum(gains[i: i + int(PERIOD)])  # Calculating sum of gains over the period
    loss = sum(losses[i: i + int(PERIOD)])  # Calculating sum of losses over the period
    gain_ave.append(gain / int(PERIOD))  # Calculate average gain and append to gain_ave
    loss_ave.append(loss / int(PERIOD))  # Calculate average loss and append to loss_ave

RSI_list = []  # List to store RSI values

# Calculate the RSI values
for i in range(len(gain_ave)):
    average_gain = gain_ave[i]
    average_loss = abs(loss_ave[i])  # Taking the absolute value of losses for RSI calculation

    # Calculate the relative strength (RS) and RSI
    if average_loss != 0:
        RS = average_gain / average_loss
        RSI = 100 - (100 / (1 + RS))
    else:
        RSI = 100  # Handling the case when average_loss is 0

    RSI_list.append(round(RSI, 4))  # Append the rounded RSI value to RSI_list

FILENAME2 = ASSET + "_" + PERIOD + "_" + RANGE + "_period_RSI_against_last_" + LIMIT + "_" + RANGE + "s"

# Write the date, time, and RSI values to a file
with open(FILENAME2, "w") as file:
    for i in range(len(RSI_list)):
        file.write(date_list[i] + ", " + time_list[i] + ", " + str(RSI_list[i]) + "\n")

print(FILENAME2)  # Print the filename



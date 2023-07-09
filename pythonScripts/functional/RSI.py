#!/usr/bin/env python3

import sys # for input
import os # for filepath
import subprocess # for subprocess

ASSET = sys.argv[1] # set the input args
CURRENCY = sys.argv[2]
LIMIT = sys.argv[3]
RANGE = sys.argv[4]
subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, LIMIT, RANGE]) # run getData.sh to create a data file

FILENAME = ASSET + "_last_" + LIMIT + "_" + RANGE +"s" # create a filename
data_file_path = os.path.join("..", "..", "data_files", FILENAME) # Create the file path

# Read the file contents
with open(data_file_path, "r") as file:
    lines = file.readlines()

price_list = []  # List to store the prices

# Extract the prices from each line
for line in lines:
    parts = line.split(", ")
    price = float(parts[1])
    price_list.append(price)

# Calculate the RSI ????
n = len(price_list)
gain_sum = 0
loss_sum = 0

for i in range(1, n):
    price_diff = price_list[i] - price_list[i - 1]
    if price_diff > 0:
        gain_sum += price_diff
    else:
        loss_sum += abs(price_diff)

avg_gain = gain_sum / (n - 1)
avg_loss = loss_sum / (n - 1)

if avg_loss == 0:
    rsi = 100  # Avoid division by zero
else:
    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

rsi = "{:05.2f}".format(rsi)
# Print the RSI
statement = ASSET + " RSI against last " + LIMIT + " " + RANGE +"s:"
print(statement, rsi)
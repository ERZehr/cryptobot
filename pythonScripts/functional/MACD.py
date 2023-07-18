#!/usr/bin/python3

import sys # for filepath

FILEPATH12 = sys.argv[1]
FILEPATH26 = sys.argv[2]
ASSET = sys.argv[3]
CURRENCY = sys.argv[4]
LIMIT = sys.argv[5]
RANGE = sys.argv[6]

# Read data from FILEPATH1 and FILEPATH2
with open(FILEPATH26, 'r') as file:
    data_26_period = [line.strip().split(', ') for line in file.readlines()]

with open(FILEPATH12, 'r') as file:
    data_12_period = [line.strip().split(', ') for line in file.readlines()]

# Perform subtraction of 26 period average from 12 period average
result_data = []
for data_26, data_12 in zip(data_26_period, data_12_period):
    date_time_26, value_26 = data_26[:2], float(data_26[2])
    date_time_12, value_12 = data_12[:2], float(data_12[2])
    result = round(value_12 - value_26, 2)
    result_data.append(date_time_26 + [str(result)])

FILENAMEEXIT = ASSET + "_MACD_last_" + LIMIT + "_" + RANGE + "s"

# Save the results in a new file
with open(FILENAMEEXIT, 'w') as file:
    for line in result_data:
        file.write(', '.join(line) + '\n')

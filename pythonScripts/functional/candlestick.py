#!/usr/bin/python3

import datetime
import cryptocompare
import sys

# Get the command-line arguments
ASSET = sys.argv[1]  # Asset ticker
CURRENCY = sys.argv[2]  # Currency
LIMIT = sys.argv[3] # number of data?
RANGE = sys.argv[4]  # minutes, hours, days

# Fetch the historical price data based on the specified range
if RANGE == "minute":
    DATA = cryptocompare.get_historical_price_minute(ASSET, currency=CURRENCY, limit=str(int(LIMIT) - 1))
elif RANGE == "hour":
    DATA = cryptocompare.get_historical_price_hour(ASSET, currency=CURRENCY, limit=str(int(LIMIT) - 1))
elif RANGE == "day":
    DATA = cryptocompare.get_historical_price_day(ASSET, currency=CURRENCY, limit=str(int(LIMIT) - 1))

list_of_lists = []  # Final list containing timestamp, open, high, low, and close value key-value pairs
for item in DATA:
    if 'time' in item and 'open' in item and 'high' in item and 'low' in item and 'close' in item:
        dt = datetime.datetime.fromtimestamp(item['time'])  # Convert timestamp to a datetime object
        list_of_lists.append([str(dt), str(item['open']), str(item['high']), str(item['low']), str(item['close'])])

filename = ASSET + "_candlestick_last_" + LIMIT + "_" + RANGE + "s"  # Generate the filename with a .csv extension
with open(filename, "w") as file:
    for sublist in list_of_lists:
        file.write(", ".join(sublist) + "\n")  # Write each sublist as a comma-separated line in the file

print(filename)  # Print the generated filename
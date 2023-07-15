#!/usr/bin/python3

ASSET = sys.argv[1]  # Cryptocurrency
CURRENCY = sys.argv[2]  # Reference currency (Typically USD)
PERIOD = int(sys.argv[3])  # Moving average period
LIMIT = int(sys.argv[4])  # Desired number of data points
RANGE = sys.argv[5]  # Day, hour, minute

filename12 = "path/to/filename12.txt"
filename26 = "path/to/filename26.txt"
output_filename = "path/to/output_macd.txt"

data12 = []
with open(filename12, 'r') as file12:
    for line in file12:
        parts = line.strip().split(', ')
        price12 = float(parts[2])
        data12.append(price12)

data26 = []
with open(filename26, 'r') as file26:
    for line in file26:
        parts = line.strip().split(', ')
        price26 = float(parts[2])
        data26.append(price26)

macd_values = [x - y for x, y in zip(data12, data26)]

with open(output_filename, 'w') as output_file:
    with open(filename12, 'r') as file12:
        for i, line in enumerate(file12):
            parts = line.strip().split(', ')
            date = parts[0]
            time = parts[1]
            output_file.write(f"{date}, {time}, {macd_values[i]}\n")

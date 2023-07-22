#!/usr/bin/python3

import sys
import os
import subprocess

ASSET = sys.argv[1]  # Cryptocurrency
CURRENCY = sys.argv[2]  # Reference currency (Typically USD)
LIMIT = int(sys.argv[3])  # Desired number of data points
RANGE = sys.argv[4]  # Day, hour, minute

subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, CURRENCY, str(LIMIT), RANGE])  # Run getData.sh to create a data file

FILENAME = ASSET + "_last_" + str(LIMIT) + "_" + RANGE + "s"  # Create a filename
data_file_path = os.path.join("..", "..", "data_files", FILENAME)  # Create the file path

hundred = None
zero = None

with open(data_file_path, "r") as file:
    for line in file:
        timestamp, value = line.strip().split(", ")
        value = float(value)

        if hundred is None or value > hundred:
            hundred = value

        if zero is None or value < zero:
            zero = value

#Math
difference = hundred - zero
seven_eight_six = difference * 0.786 + zero
six_one_eight = difference * 0.618 + zero
fifty = difference * 0.5 + zero
three_eighty_two = difference * 0.382 + zero

FILENAME2 =  ASSET + "_fibonacci_last_" + str(LIMIT) + "_" + RANGE + "s" # create filename

with open(FILENAME2, 'w') as file:
    file.write(f"{round(hundred, 5)}\n")
    file.write(f"{round(seven_eight_six, 5)}\n")
    file.write(f"{round(six_one_eight, 5)}\n")
    file.write(f"{round(fifty, 5)}\n")
    file.write(f"{round(three_eighty_two, 5)}\n")
    file.write(f"{round(zero, 5)}\n")


os.environ["FILENAME"] = FILENAME  # Set the value of FILENAME2 as an environment variable
subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
print(FILENAME2)  # Print the name of the new file
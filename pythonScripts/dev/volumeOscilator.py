#!/usr/bin/python3

import sys
import os
import subprocess

ASSET = sys.argv[1]  # Cryptocurrency
CURRENCY = sys.argv[2]  # Reference currency (Typically USD)
LIMIT = int(sys.argv[3])  # Desired number of data points
RANGE = sys.argv[4]  # Day, hour, minute

if RANGE == "minute":
    USDAVE = []
    KRWAVE = []
    JPYAVE = []
    EURAVE = []
    # get average prices over the hour period
    # for USD
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "USD", str((LIMIT + 1)), "minute"])  # Run getData.sh to create a data file
    FILENAMEUSD = ASSET + "_" + "last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEUSD = os.path.join("..", "..", "data_files", FILENAMEUSD)  # Create the file path
    with open(FILENAMEUSD, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        USDAVE.append(value)
    os.environ["FILENAME"] = FILENAMEUSD  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for KRW
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "KRW", str((LIMIT + 1)), "minute"])  # Run getData.sh to create a data file
    FILENAMEKRW = ASSET + "_" + "last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRW = os.path.join("..", "..", "data_files", FILENAMEKRW)  # Create the file path
    with open(FILENAMEKRW, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        KRWAVE.append(value)
    os.environ["FILENAME"] = FILENAMEKRW  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for JPY
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "JPY", str((LIMIT + 1)), "minute"])  # Run getData.sh to create a data file
    FILENAMEJPY = ASSET + "_" + "last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPY = os.path.join("..", "..", "data_files", FILENAMEJPY)  # Create the file path
    with open(FILENAMEJPY, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        JPYAVE.append(value)
    os.environ["FILENAME"] = FILENAMEJPY  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for EUR
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "EUR", str((LIMIT + 1)), "minute"])  # Run getData.sh to create a data file
    FILENAMEEUR = ASSET + "_" + "last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEUR = os.path.join("..", "..", "data_files", FILENAMEEUR)  # Create the file path
    with open(FILENAMEEUR, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        EURAVE.append(value)
    os.environ["FILENAME"] = FILENAMEEUR  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # at this point we should have the average price for each hour
    # query both types of volume data
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "USD", str((LIMIT + 1)), RANGE])  # get USD volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "KRW", str((LIMIT + 1)), RANGE])  # get KRW volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "JPY", str((LIMIT + 1)), RANGE])  # get JPY volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "EUR", str((LIMIT + 1)), RANGE])  # get EUR volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "USD", str((LIMIT + 1)), RANGE])  # get USD volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "KRW", str((LIMIT + 1)), RANGE])  # get KRW volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "JPY", str((LIMIT + 1)), RANGE])  # get JPY volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "EUR", str((LIMIT + 1)), RANGE])  # get EUR volumeTo
    # create filenames for all reads
    FILENAMEUSDF = ASSET + "_USD_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRWF = ASSET + "_KRW_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPYF = ASSET + "_JPY_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEURF = ASSET + "_EUR_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEUSDT = ASSET + "_USD_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRWT = ASSET + "_KRW_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPYT = ASSET + "_JPY_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEURT = ASSET + "_EUR_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    # create lists for all data
    USDFrom = []
    KRWFrom = []
    JPYFrom = []
    EURFrom = []
    USDTo = []
    KRWTo = []
    JPYTo = []
    EURTo = []
    datetime = []
    # Read data into lists using a for loop
    FILENAMEUSDF = os.path.join("..", "..", "data_files", FILENAMEUSDF)  # Create the file path
    with open(FILENAMEUSDF, "r") as file:
        for line in file:
            time, value = line.strip().split(", ")
            USDFrom.append(float(value))
            datetime.append(time) # the date and time for the file is set here
    os.environ["FILENAME"] = FILENAMEUSDF  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEKRWF = os.path.join("..", "..", "data_files", FILENAMEKRWF)  # Create the file path
    with open(FILENAMEKRWF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            KRWFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEKRWF  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEJPYF = os.path.join("..", "..", "data_files", FILENAMEJPYF)  # Create the file path
    with open(FILENAMEJPYF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            JPYFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEJPYF  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEEURF = os.path.join("..", "..", "data_files", FILENAMEEURF)  # Create the file path
    with open(FILENAMEEURF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            EURFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEEURF  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEUSDT = os.path.join("..", "..", "data_files", FILENAMEUSDT)  # Create the file path
    with open(FILENAMEUSDT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            USDTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEUSDT  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEKRWT = os.path.join("..", "..", "data_files", FILENAMEKRWT)  # Create the file path
    with open(FILENAMEKRWT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            KRWTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEKRWT  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEJPYT = os.path.join("..", "..", "data_files", FILENAMEJPYT)  # Create the file path
    with open(FILENAMEJPYT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            JPYTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEJPYT  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEEURT = os.path.join("..", "..", "data_files", FILENAMEEURT)  # Create the file path
    with open(FILENAMEEURT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            EURTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEEURT  # Set the value of FILENAME as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # at this point, we should have all the volume files read into lists
    # do conversions
    USDTADJ = []
    KRWTADJ = []
    JPYTADJ = []
    EURTADJ = []
    for i in range((LIMIT + 1)): # loop through the lists of data to calc adjusted numbers
        USDTADJ.append(USDTo[i] / USDAVE[i])
        KRWTADJ.append(KRWTo[i] / KRWAVE[i])
        JPYTADJ.append(JPYTo[i] / JPYAVE[i])
        EURTADJ.append(EURTo[i] / EURAVE[i])

    difference = []
    for i in range((LIMIT + 1)): # loop throught to find difference in to and from
        difference.append((USDTADJ[i] + KRWTADJ[i] + JPYTADJ[i] + EURTADJ[i]) - (USDFrom[i] + KRWFrom[i] + JPYFrom[i] + EURFrom[i]))

    # at the end, write back to file
    FILENAME2 = ASSET + "_volumeTO_last_" + str(LIMIT) + "_" + RANGE + "s" # create filename

    with open(FILENAME2, 'w') as file:
        for i in range(LIMIT):
            file.write(f"{datetime[i]}, {difference[i]}\n")

    print(FILENAME2)  # Print the name of the new file





elif RANGE == "hour":
    N = 60  # Number of points in average
    total = 0
    count = 0
    USDAVE = []
    KRWAVE = []
    JPYAVE = []
    EURAVE = []
    # get average prices over the hour period
    # for USD
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "USD", str((LIMIT + 1) * 60), "minute"])  # Run getData.sh to create a data file
    FILENAMEUSD = ASSET + "_" + "last_" + str((LIMIT + 1) * 60) + "_minutes" # generate filename
    FILENAMEUSD = os.path.join("..", "..", "data_files", FILENAMEUSD)  # Create the file path
    with open(FILENAMEUSD, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            USDAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEUSD  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for KRW
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "KRW", str((LIMIT + 1) * 60), "minute"])  # Run getData.sh to create a data file
    FILENAMEKRW = ASSET + "_" + "last_" + str((LIMIT + 1) * 60) + "_minutes" # generate filename
    FILENAMEKRW = os.path.join("..", "..", "data_files", FILENAMEKRW)  # Create the file path
    with open(FILENAMEKRW, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            KRWAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEKRW  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for JPY
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "JPY", str((LIMIT + 1) * 60), "minute"])  # Run getData.sh to create a data file
    FILENAMEJPY = ASSET + "_" + "last_" + str((LIMIT + 1) * 60) + "_minutes" # generate filename
    FILENAMEJPY = os.path.join("..", "..", "data_files", FILENAMEJPY)  # Create the file path
    with open(FILENAMEJPY, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            JPYAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEJPY  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for EUR
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "EUR", str((LIMIT + 1) * 60), "minute"])  # Run getData.sh to create a data file
    FILENAMEEUR = ASSET + "_" + "last_" + str((LIMIT + 1) * 60) + "_minutes" # generate filename
    FILENAMEEUR = os.path.join("..", "..", "data_files", FILENAMEEUR)  # Create the file path
    with open(FILENAMEEUR, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            EURAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEEUR  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # at this point we should have the average price for each hour
    # query both types of volume data
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "USD", str((LIMIT + 1)), RANGE])  # get USD volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "KRW", str((LIMIT + 1)), RANGE])  # get KRW volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "JPY", str((LIMIT + 1)), RANGE])  # get JPY volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "EUR", str((LIMIT + 1)), RANGE])  # get EUR volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "USD", str((LIMIT + 1)), RANGE])  # get USD volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "KRW", str((LIMIT + 1)), RANGE])  # get KRW volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "JPY", str((LIMIT + 1)), RANGE])  # get JPY volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "EUR", str((LIMIT + 1)), RANGE])  # get EUR volumeTo
    # create filenames for all reads
    FILENAMEUSDF = ASSET + "_USD_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRWF = ASSET + "_KRW_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPYF = ASSET + "_JPY_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEURF = ASSET + "_EUR_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEUSDT = ASSET + "_USD_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRWT = ASSET + "_KRW_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPYT = ASSET + "_JPY_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEURT = ASSET + "_EUR_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    # create lists for all data
    USDFrom = []
    KRWFrom = []
    JPYFrom = []
    EURFrom = []
    USDTo = []
    KRWTo = []
    JPYTo = []
    EURTo = []
    datetime = []
    # Read data into lists using a for loop
    FILENAMEUSDF = os.path.join("..", "..", "data_files", FILENAMEUSDF)  # Create the file path
    with open(FILENAMEUSDF, "r") as file:
        for line in file:
            time, value = line.strip().split(", ")
            USDFrom.append(float(value))
            datetime.append(time) # the date and time for the file is set here
    os.environ["FILENAME"] = FILENAMEUSDF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEKRWF = os.path.join("..", "..", "data_files", FILENAMEKRWF)  # Create the file path
    with open(FILENAMEKRWF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            KRWFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEKRWF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEJPYF = os.path.join("..", "..", "data_files", FILENAMEJPYF)  # Create the file path
    with open(FILENAMEJPYF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            JPYFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEJPYF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEEURF = os.path.join("..", "..", "data_files", FILENAMEEURF)  # Create the file path
    with open(FILENAMEEURF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            EURFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEEURF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEUSDT = os.path.join("..", "..", "data_files", FILENAMEUSDT)  # Create the file path
    with open(FILENAMEUSDT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            USDTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEUSDT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEKRWT = os.path.join("..", "..", "data_files", FILENAMEKRWT)  # Create the file path
    with open(FILENAMEKRWT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            KRWTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEKRWT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEJPYT = os.path.join("..", "..", "data_files", FILENAMEJPYT)  # Create the file path
    with open(FILENAMEJPYT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            JPYTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEJPYT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEEURT = os.path.join("..", "..", "data_files", FILENAMEEURT)  # Create the file path
    with open(FILENAMEEURT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            EURTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEEURT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # at this point, we should have all the volume files read into lists
    # do conversions
    USDTADJ = []
    KRWTADJ = []
    JPYTADJ = []
    EURTADJ = []
    for i in range((LIMIT + 1)): # loop through the lists of data to calc adjusted numbers
        USDTADJ.append(USDTo[i] / USDAVE[i])
        KRWTADJ.append(KRWTo[i] / KRWAVE[i])
        JPYTADJ.append(JPYTo[i] / JPYAVE[i])
        EURTADJ.append(EURTo[i] / EURAVE[i])

    difference = []
    for i in range((LIMIT + 1)): # loop throught to find difference in to and from
        difference.append((USDTADJ[i] + KRWTADJ[i] + JPYTADJ[i] + EURTADJ[i]) - (USDFrom[i] + KRWFrom[i] + JPYFrom[i] + EURFrom[i]))

    # at the end, write back to file
    FILENAME2 = ASSET + "_volumeTO_last_" + str((LIMIT)) + "_" + RANGE + "s" # create filename

    with open(FILENAME2, 'w') as file:
        for i in range(LIMIT):
            file.write(f"{datetime[i]}, {difference[i]}\n")

    print(FILENAME2)  # Print the name of the new file






elif RANGE == "day":
    N = 24  # Number of points in average
    total = 0
    count = 0
    USDAVE = []
    KRWAVE = []
    JPYAVE = []
    EURAVE = []
    # get average prices over the hour period
    # for USD
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "USD", str((LIMIT + 1) * 24), "hour"])  # Run getData.sh to create a data file
    FILENAMEUSD = ASSET + "_" + "last_" + str((LIMIT + 1) * 24) + "_hours" # generate filename
    FILENAMEUSD = os.path.join("..", "..", "data_files", FILENAMEUSD)  # Create the file path
    with open(FILENAMEUSD, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            USDAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEUSD  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for KRW
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "KRW", str((LIMIT + 1) * 24), "hour"])  # Run getData.sh to create a data file
    FILENAMEKRW = ASSET + "_" + "last_" + str((LIMIT + 1) * 24) + "_hours" # generate filename
    FILENAMEKRW = os.path.join("..", "..", "data_files", FILENAMEKRW)  # Create the file path
    with open(FILENAMEKRW, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            KRWAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEKRW  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for JPY
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "JPY", str((LIMIT + 1) * 24), "hour"])  # Run getData.sh to create a data file
    FILENAMEJPY = ASSET + "_" + "last_" + str((LIMIT + 1) * 24) + "_hours" # generate filename
    FILENAMEJPY = os.path.join("..", "..", "data_files", FILENAMEJPY)  # Create the file path
    with open(FILENAMEJPY, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            JPYAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEJPY  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # for EUR
    subprocess.run(["bash", "../../bashScripts/functional/getData.sh", ASSET, "EUR", str((LIMIT + 1) * 24), "hour"])  # Run getData.sh to create a data file
    FILENAMEEUR = ASSET + "_" + "last_" + str((LIMIT + 1) * 24) + "_hours" # generate filename
    FILENAMEEUR = os.path.join("..", "..", "data_files", FILENAMEEUR)  # Create the file path
    with open(FILENAMEEUR, "r") as file:
        data = file.readlines()
    for line in data: # average up the data points
        timestamp, value = line.strip().split(", ")
        value = float(value)
        total += value
        count += 1
        if count == N:
            average = total / N
            EURAVE.append(average)
            total = 0
            count = 0
    os.environ["FILENAME"] = FILENAMEEUR  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # at this point we should have the average price for each hour
    # query both types of volume data
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "USD", str((LIMIT + 1)), RANGE])  # get USD volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "KRW", str((LIMIT + 1)), RANGE])  # get KRW volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "JPY", str((LIMIT + 1)), RANGE])  # get JPY volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeFrom.sh", ASSET, "EUR", str((LIMIT + 1)), RANGE])  # get EUR volumeFrom
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "USD", str((LIMIT + 1)), RANGE])  # get USD volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "KRW", str((LIMIT + 1)), RANGE])  # get KRW volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "JPY", str((LIMIT + 1)), RANGE])  # get JPY volumeTo
    subprocess.run(["bash", "../../bashScripts/functional/volumeTo.sh", ASSET, "EUR", str((LIMIT + 1)), RANGE])  # get EUR volumeTo
    # create filenames for all reads
    FILENAMEUSDF = ASSET + "_USD_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRWF = ASSET + "_KRW_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPYF = ASSET + "_JPY_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEURF = ASSET + "_EUR_volumeFrom_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEUSDT = ASSET + "_USD_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEKRWT = ASSET + "_KRW_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEJPYT = ASSET + "_JPY_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    FILENAMEEURT = ASSET + "_EUR_volumeTo_last_" + str((LIMIT + 1)) + "_" + RANGE + "s" # generate filename
    # create lists for all data
    USDFrom = []
    KRWFrom = []
    JPYFrom = []
    EURFrom = []
    USDTo = []
    KRWTo = []
    JPYTo = []
    EURTo = []
    datetime = []
    # Read data into lists using a for loop
    FILENAMEUSDF = os.path.join("..", "..", "data_files", FILENAMEUSDF)  # Create the file path
    with open(FILENAMEUSDF, "r") as file:
        for line in file:
            time, value = line.strip().split(", ")
            USDFrom.append(float(value))
            datetime.append(time) # the date and time for the file is set here
    os.environ["FILENAME"] = FILENAMEUSDF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEKRWF = os.path.join("..", "..", "data_files", FILENAMEKRWF)  # Create the file path
    with open(FILENAMEKRWF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            KRWFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEKRWF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEJPYF = os.path.join("..", "..", "data_files", FILENAMEJPYF)  # Create the file path
    with open(FILENAMEJPYF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            JPYFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEJPYF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEEURF = os.path.join("..", "..", "data_files", FILENAMEEURF)  # Create the file path
    with open(FILENAMEEURF, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            EURFrom.append(float(value))
    os.environ["FILENAME"] = FILENAMEEURF  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEUSDT = os.path.join("..", "..", "data_files", FILENAMEUSDT)  # Create the file path
    with open(FILENAMEUSDT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            USDTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEUSDT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEKRWT = os.path.join("..", "..", "data_files", FILENAMEKRWT)  # Create the file path
    with open(FILENAMEKRWT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            KRWTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEKRWT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEJPYT = os.path.join("..", "..", "data_files", FILENAMEJPYT)  # Create the file path
    with open(FILENAMEJPYT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            JPYTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEJPYT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file

    FILENAMEEURT = os.path.join("..", "..", "data_files", FILENAMEEURT)  # Create the file path
    with open(FILENAMEEURT, "r") as file:
        for line in file:
            _, value = line.strip().split(", ")
            EURTo.append(float(value))
    os.environ["FILENAME"] = FILENAMEEURT  # Set the value of FILENAME2 as an environment variable
    subprocess.run(["bash", "-c", "rm -f ../../data_files/$FILENAME"])  # Run the subprocess to remove the file
    # at this point, we should have all the volume files read into lists
    # do conversions
    USDTADJ = []
    KRWTADJ = []
    JPYTADJ = []
    EURTADJ = []
    for i in range((LIMIT + 1)): # loop through the lists of data to calc adjusted numbers
        USDTADJ.append(USDTo[i] / USDAVE[i])
        KRWTADJ.append(KRWTo[i] / KRWAVE[i])
        JPYTADJ.append(JPYTo[i] / JPYAVE[i])
        EURTADJ.append(EURTo[i] / EURAVE[i])

    difference = []
    for i in range((LIMIT + 1)): # loop throught to find difference in to and from
        difference.append((USDTADJ[i] + KRWTADJ[i] + JPYTADJ[i] + EURTADJ[i]) - (USDFrom[i] + KRWFrom[i] + JPYFrom[i] + EURFrom[i]))

    # at the end, write back to file
    FILENAME2 = ASSET + "_volumeTO_last_" + str(LIMIT) + "_" + RANGE + "s" # create filename

    with open(FILENAME2, 'w') as file:
        for i in range(LIMIT):
            file.write(f"{datetime[i]}, {difference[i]}\n")

    print(FILENAME2)  # Print the name of the new file


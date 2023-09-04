#!/usr/bin/python3

# This simulation will trade BTC, ETC, DOGE, ETH, LTC, and BCH solely on the last digit of MACD indicator data

import os
import subprocess
import json
import re
import time

INVEST_FRACTION = 0.2

loop_assets = ["BTC", "ETC", "DOGE", "ETH", "LTC", "BCH"] # assets we are considering
values_old = {"BTC":0, "ETC":0, "DOGE":0, "ETH":0, "LTC":0, "BCH":0} # for the old values
values_new = {"BTC":0, "ETC":0, "DOGE":0, "ETH":0, "LTC":0, "BCH":0} # for our new comparitive values

while(1):
    # get the MACD data
    for currency in loop_assets: # for each currency, find the latest MACD data
        os.chdir("../functional")
        subprocess.run(["bash", "./MACD.sh", currency, "USD", "26", "minute"])
        filename =  "../../data_files/" + currency + "_MACD_last_26_minutes"
        with open(filename, 'r') as file:
            counter = 0
            for line in file:
                counter += 1
                if counter == 26:
                    parts = line.strip().split(', ')
                    values_new[currency] = parts[2] # put the last MACD data into the values_new dict
        os.environ["FILENAME"] = filename
        subprocess.run(["bash", "-c", "rm -f $FILENAME"])
    
    # import json data
    filepath = "/home/lucky/ccurency/cryptobot/admin/accountData/Sim.json"  # Set the value of FILENAME as an environment variable
    with open(filepath, 'r+') as userFile:  # Open the JSON file
        userFileData = json.load(userFile)  # Load the JSON file
        jsonFile = dict(userFileData)
        total_cash = jsonFile['cash']
        userFile.seek(0)  # Move the file pointer to the beginning

    # make decisions
    for currency in loop_assets:
        print(currency, values_new[currency])
        if float(values_new[currency]) > 0 and float(values_old[currency]) <= 0: # if we break zero up
            to_spend = INVEST_FRACTION * total_cash
            total_cash -= to_spend
            os.environ["FILENAME"] = "/home/lucky/ccurency/cryptobot/bashScripts/trade/trade.sh" # Set the value of FILENAME as an environment variable
            subprocess.run(["bash", "-c", "$FILENAME " + currency + " " + str(to_spend) + " buy market_order_cash none Sim"])
        elif float(values_new[currency]) <= 0 and float(values_old[currency]) > 0 and currency in jsonFile["assets"] and jsonFile["assets"][currency] > 0: # if we break zero down and we have the asset
            total_assets = jsonFile["assets"][currency]
            os.environ["FILENAME"] = "/home/lucky/ccurency/cryptobot/bashScripts/trade/trade.sh"  # Set the value of FILENAME as an environment variable
            subprocess.run(["bash", "-c", "$FILENAME " + currency + " none sell sell_all none Sim"])        
    
    values_old = dict(values_new) # make new values old values
    os.chdir("../functional")
    time.sleep(300)

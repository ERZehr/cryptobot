import os
import subprocess
import json
import re
from datetime import datetime, timedelta

# For standard market order
def marketOrder(currency, quantity, user):
    # Get the price and calculate the sale
    command = ["python3", "../functional/getCurrentPrice.py", currency, "USD"]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = re.findall(r'\d+\.\d+', completed_process.stdout)
    price = float(result[0]) # Convert the output to a float
    buyPrice = price * float(quantity)

    # Read user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r') as userFile:  # Open the JSON file in read mode
        userFileData = json.load(userFile)  # Load the JSON file

    # Check for funds, update cash and assets
    if 'cash' not in userFileData:
        userFileData['cash'] = float(0)
    if userFileData['cash'] < buyPrice:
        print("Not Enough Funds!")
    elif userFileData['cash'] >= buyPrice:
        if 'assets' not in userFileData:
            userFileData['assets'] = {}
        if currency in userFileData['assets']:
            userFileData['assets'][currency] += float(quantity)
        else:
            userFileData['assets'][currency] = float(quantity)
        userFileData['cash'] -= buyPrice

        # write changes to json file
        with open(filepath, 'w') as userFile:
            json.dump(userFileData, userFile, indent=4)

        # terminal notification 
        print("Bought " + str(quantity) + " " + currency + " at $" + str(price) + " per " + currency + ". Total Cost: $" + str(buyPrice))


# For limit order
def limitOrder(currency, quantity, line, user):
    # Read the user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r') as userFile:  # Open the JSON file in read mode
        userFileData = json.load(userFile)  # Load the JSON file

    # create edits to file
    if 'actions' not in userFileData:
        userFileData['actions'] = {}
    key_to_insert = 0
    while str(key_to_insert) in userFileData['actions']:
        key_to_insert += 1
    userFileData['actions'][str(key_to_insert)] = {
    "asset": currency,
    "action": "buy",
    "type": "limit",
    "quantity": float(quantity),
    "line": float(line)
    }
    
    # write changes to json file
    with open(filepath, 'w') as userFile:
        json.dump(userFileData, userFile, indent=4)

    # terminal notification    
    print("Placed limit order to buy " + currency + " at $" + str(line) + " per " + currency + ".")
    

# For stop order
def stopOrder(currency, quantity, line, user):
    # Read the user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r') as userFile:  # Open the JSON file in read mode
        userFileData = json.load(userFile)  # Load the JSON file

    # create edits to file
    if 'actions' not in userFileData:
        userFileData['actions'] = {}
    key_to_insert = 0
    while str(key_to_insert) in userFileData['actions']:
        key_to_insert += 1
    userFileData['actions'][str(key_to_insert)] = {
    "asset": currency,
    "action": "buy",
    "type": "stop",
    "quantity": float(quantity),
    "line": float(line)
    }
    
    # write changes to json file
    with open(filepath, 'w') as userFile:
        json.dump(userFileData, userFile, indent=4)

    # terminal notification    
    print("Placed stop order to buy " + currency + " at $" + str(line) + " per " + currency + ".")


# For market order with cash quantity
def marketOrderCash(currency, cash, user):
    # Get the price and calculate the sale quantity
    command = ["python3", "../functional/getCurrentPrice.py", currency, "USD"]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = re.findall(r'\d+\.\d+', completed_process.stdout)
    price = float(result[0]) # Convert the output to a float
    quantity = float(cash) / price # number of shares to buy

    # Read the user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r') as userFile:  # Open the JSON file
        userFileData = json.load(userFile)  # Load the JSON file

    #Check for funds, update cash and assets
    if 'cash' not in userFileData:
        userFileData['cash'] = float(0)
    if userFileData['cash'] < float(cash):
        print("Not Enough Funds!")
    elif userFileData['cash'] >= float(cash):
        if 'assets' not in userFileData:
            userFileData['assets'] = {}
        if currency in userFileData['assets']:
            userFileData['assets'][currency] += float(quantity)
        else:
            userFileData['assets'][currency] = float(quantity)
        userFileData['cash'] -= float(cash)

        # write changes to json file
        with open(filepath, 'w') as userFile:
            json.dump(userFileData, userFile, indent=4)

        # terminal notification    
        print("Bought " + str(quantity) + " " + currency + " at $" + str(price) + " per " + currency + ". Total Cost: $" + str(cash))



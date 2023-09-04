import os
import subprocess
import json
import re


# For standard market order
def marketOrder(currency, quantity, user):
    # Get the price and calculate the sale
    command = ["python3", "../functional/getCurrentPrice.py", currency, "USD"]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = re.findall(r'\d+\.\d+', completed_process.stdout)
    price = float(result[0])  # Convert the output to a float
    sellPrice = price * float(quantity)

    # Read user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r') as userFile:  # Open the JSON file in read mode
        userFileData = json.load(userFile)  # Load the JSON file

    # Check if the asset exists and if there's enough quantity to sell
    if 'assets' not in userFileData or currency not in userFileData['assets'] or userFileData['assets'][currency] < float(quantity):
        print("Not Enough Assets to Sell!")
    else:
        # Update the asset quantity and increase the cash
        userFileData['assets'][currency] -= float(quantity)
        userFileData['cash'] += float(sellPrice)

        # write changes to json file
        with open(filepath, 'w') as userFile:
            json.dump(userFileData, userFile, indent=4)

        # terminal notification 
        print("Sold " + str(quantity) + " " + currency + " at $" + str(price) + " per " + currency + ". Total Profit: $" + str(sellPrice))


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
    "action": "sell",
    "type": "limit",
    "quantity": float(quantity),
    "line": float(line)
    }
    
    # write changes to json file
    with open(filepath, 'w') as userFile:
        json.dump(userFileData, userFile, indent=4)

    # terminal notification    
    print("Placed limit order to sell " + currency + " at $" + str(line) + " per " + currency + ".")


def stopOrder(currency, quantity, line, user): # for stop order
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
    "action": "sell",
    "type": "stop",
    "quantity": float(quantity),
    "line": float(line)
    }
    
    # write changes to json file
    with open(filepath, 'w') as userFile:
        json.dump(userFileData, userFile, indent=4)

    # terminal notification    
    print("Placed stop order to sell " + currency + " at $" + str(line) + " per " + currency + ".")


def sellAll(currency, user):
    # Get the price and calculate the sale
    command = ["python3", "../functional/getCurrentPrice.py", currency, "USD"]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = re.findall(r'\d+\.\d+', completed_process.stdout)
    price = float(result[0]) # Convert the output to a float

    # Read the user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r+') as userFile:  # Open the JSON file
        userFileData = json.load(userFile)  # Load the JSON file

    # Check if the asset exists and if there's any to sell
    if 'assets' not in userFileData or currency not in userFileData['assets'] or userFileData['assets'][currency] == 0:
        print("No " + currency + " to Sell!")
    else:
        # Update the asset quantity and increase the cash
        total_sale = price * userFileData['assets'][currency]
        userFileData['cash'] += total_sale
        quantity = userFileData['assets'][currency]
        userFileData['assets'][currency] -= quantity

        # write changes to json file
        with open(filepath, 'w') as userFile:
            json.dump(userFileData, userFile, indent=4)

        # terminal notification    
        print("Sold " + str(quantity) + " " + currency + " at $" + str(price) + " per " + currency + ". Total Profit: $" + str(total_sale))


'''def marketOrderCash(currency, cash, user):
    # Get the price and calculate the sale
    command = ["python3", "../functional/getCurrentPrice.py", currency, "USD"]
    completed_process = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    result = re.findall(r'\d+\.\d+', completed_process.stdout)
    price = float(result[0]) # Convert the output to a float

    # Write the purchase to the user file
    filepath = '../../admin/accountData/' + user + '.json'
    with open(filepath, 'r+') as userFile:  # Open the JSON file
        userFileData = json.load(userFile)  # Load the JSON file

        # Check if the asset exists and if there's enough quantity to sell
        if 'assets' not in userFileData or currency not in userFileData['assets']: # We still need to check for enough crypto HERE
            print("Not Enough " + currency + " to Sell!")
        else:
            # Update the asset quantity and increase the cash
            total_sale = price * userFileData['assets'][currency]
            userFileData['cash'] += total_sale
            quantity = userFileData['assets'][currency]
            userFileData['assets'][currency] -= quantity

        # Update the JSON data in the file
        userFile.seek(0)  # Move the file pointer to the beginning
        json.dump(userFileData, userFile, indent=4)  # Write the updated data with proper formatting
    print("Sold " + str(quantity) + " " + currency + " at $" + str(price) + " per " + currency + ". Total Profit: $" + str(total_sale))'''
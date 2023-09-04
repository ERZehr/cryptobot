#!/usr/bin/python3

import sys # for inputs
import json

Cash = sys.argv[1]
Assets = sys.argv[2]
Actions = sys.argv[3]

# Open the user file
filepath = '../../admin/accountData/Sim.json'
with open(filepath, 'r+') as userFile:  # Open the JSON file
    userFileData = json.load(userFile)  # Load the JSON file

    userFileData['cash'] = float(Cash)
    userFileData['assets'] = {}
    userFileData['actions'] = {}

    # Update the JSON data in the file
    userFile.seek(0)  # Move the file pointer to the beginning
    json.dump(userFileData, userFile, indent=4)  # Write the updated data with proper formatting
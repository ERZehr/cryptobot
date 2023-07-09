#!/usr/bin/python3

import datetime
import sys
import yfinance
import json


asset = input("Enter Asset: ")


#from last year
start = datetime.datetime(2021,8,19)
end = datetime.datetime.now()

#Get file, convert to JSON, and set up sorting
asset = yfinance.download('%s-USD' % asset, start, end)
asset_json = asset.to_json()
assetFile = open("%s.txt" % asset, 'w')
assetFile.write(asset_json)
assetFile.close()
assetFile = open("%s.txt" % asset, 'r')
asset_file = json.load(assetFile)


#Sort File
SortedBTCFile = open("%sHistorySorted.txt" % asset, 'w')
SortedBTCFile.write("")
SortedBTCF.close()
SortedBTCFile = open("%sHistorySorted.txt" % asset, 'a')
for i in range(365):
	SortedBTCFile.write(str(asset_file["Open"][str(1629417600000 + (i * 86400000))]) + "," + str(asset_file["High"][str(1629417600000 + (i * 86400000))]) + "," + str(asset_file["Low"][str(1629417600000 + (i * 86400000))]) + "," + str(asset_file["Close"][str(1629417600000 + (i * 86400000))]) + "," + str(asset_file["Adj Close"][str(1629417600000 + (i * 86400000))]) + "," + str(asset_file["Volume"][str(1629417600000 + (i * 86400000))]) + "\n")
SortedBTCFile.close()
BTCFile.close()


#Math with data

#Volatility
'''dataFile = open("BTCHistory.txt", 'r')
PriceTotal = 0
for lines in dataFile:
	PriceTotal += lines.strip("\n").split(',')[1]
Pav = PriceTotal/365.0
'''


#All this math will be long term data points: Volatility, 
#Need to figure out how much data we want or make a start parameter
#fix the whole file too long error
# fix the wierd number system for cleaning the file
#

#!/usr/bin/python3
import datetime
import cryptocompare
import sys

#Funtion Implementation	




#Function to buy assets
def buy(Trader, asset, quantity, unitPrice, time):
	#[SYNTAX] lines.strip("\n").split(',')[item#]
	total = float(quantity) * unitPrice
	assetFile = open("%s_assets.txt" % Trader, 'r')	
	assetLines = assetFile.readlines()
	
	#Funds test
	if total > float(assetLines[0].strip("\n").split(',')[2]):
		print("Not enough funds you broke dumbass.")
		assetFile.close()
		return
	else:
		assetFile.close()
	
	#Send order to exchange here
		
	#Buying more of an already owned asset
	ledgerFile = open("%s_ledger.txt" % Trader, 'a')
	assetFile = open("%s_assets.txt" % Trader, 'r')	
	assetLines = assetFile.readlines()
	counter = 0
	for lines in assetLines:
		if lines.strip("\n").split(',')[0] == asset:
			oldQuantity = lines.strip("\n").split(',')[1]
			oldTotal = lines.strip("\n").split(',')[2]
			newQuantity = float(oldQuantity) + float(quantity)
			newTotal = float(oldTotal) + float(total)
			assetLines[0] = "USD," + str(float(assetLines[0].split(',')[1]) - float(total)) + "," + str(float(assetLines[0].split(',')[2]) - float(total)) + "\n"
			assetLines[counter] = asset + "," + str(newQuantity) + "," + str(newTotal) + "\n"
			assetFile.close()
			assetFile = open("%s_assets.txt" % Trader, 'w')	
			assetFile.writelines(assetLines)
			assetFile.close()
			ledgerFile.write("Purchase: " + asset + "   Qty: " + str(quantity) + "   Unit Cost: " + str(unitPrice) + "   Total: " + str(total) + "   Time: " + str(time) + "\n")
			ledgerFile.close()
			return
		counter +=1
	
	#Buying a new asset
	assetFile.close()
	assetFile = open("%s_assets.txt" % Trader, 'r')
	assetLines = assetFile.readlines()
	assetLines[0] = "USD," + str(float(assetLines[0].split(',')[1]) - float(total)) + "," + str(float(assetLines[0].split(',')[2]) - float(total)) + "\n"
	assetFile.close()
	assetFile = open("%s_assets.txt" % Trader, 'w')	
	assetFile.writelines(assetLines)
	assetFile.close()
	assetFile = open("%s_assets.txt" % Trader, 'a')
	assetFile.write(asset + "," + str(quantity) + "," + str(total) + "\n")
	assetFile.close()
	ledgerFile.write("Purchase: " + asset + "   Qty: " + str(quantity )+ "   Unit Cost: " + str(unitPrice) + "   Total: " + str(total) + "   Time: " + str(time)+ "\n")
	ledgerFile.close()	
	
	




#Function to sell assets
def sell(Trader, asset, quantity, unitPrice, time):
	assetFile = open("%s_assets.txt" % Trader, 'r')	
	assetLines = assetFile.readlines()
	counter = 0
	for lines in assetLines:
		line = lines.strip("\n").split(',')
		if line[0] == asset:
			if line[1] < quantity:
				print("You do not own enough " + line[0])
				return
			else:
				#Send Order to exchange here
				
				total = float(quantity) * unitPrice
				oldQuantity = lines.strip("\n").split(',')[1]
				oldTotal = lines.strip("\n").split(',')[2]
				newQuantity = float(oldQuantity) - float(quantity)
				newTotal = float(oldTotal) - float(total)
				assetLines[0] = "USD," + str(float(assetLines[0].split(',')[1]) + float(total)) + "," + str(float(assetLines[0].split(',')[2]) + float(total)) + "\n"
				assetLines[counter] = asset + "," + str(newQuantity) + "," + str(newTotal) + "\n"
				assetFile.close()
				assetFile = open("%s_assets.txt" % Trader, 'w')	
				assetFile.writelines(assetLines)
				assetFile.close()
				ledgerFile = open("%s_ledger.txt" % Trader, 'a')
				ledgerFile.write("Sale: " + asset + "   Qty: " + str(quantity) + "   Unit Cost: " + str(unitPrice) + "   Total: " + str(total) + "   Time: " + str(time) + "\n")
				ledgerFile.close()
				return
		counter += 1
	print("You do not own any " + asset)	







	for ownedAssets in assetFile:
		if asset == ownedAsset[0]:
			if quantity <= ownedAssets[2]:
				total = quantity * unitPrice
				assetFile[0].write("USD," + (assetFileLines[0].split(',')[1] + total) + "," + (assetFileLInes[0].split(',')[2] + total))
				ownedAssets.write(asset + "," + (ownedAssets.split(',')[1] - total) + "," + (ownedAssets.split(',')[2] - quantity))
				ledgerFile.append(["Sale: ", asset, quantity, unitPrice, time])
				assetFile.close()
				ledgerFile.close
			else:
				print("You do not own enough " + ownedAsset[0])
		else:
			print("You do not hold and " + ownedAssets[0])
		
			

#Funtion to view held assets	
def viewAssets(assetFile):	
	assetLines = assetFile.readlines()
	counter = 0
	for lines in assetLines:
		print(lines)
		counter += 1
	if counter == 0:
		print("You have no assets.")

	
#Function to view trade ledger
def viewLedger(ledgerFile):
	ledgerLines = ledgerFile.readlines()
	counter = 0
	for lines in ledgerLines:
		print(lines)
		counter += 1
	if counter == 0:
		print("There is nothing in your ledger")


			
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------		
#Logic Exchange Engine
try:
	Trader = sys.argv[1]
	Action = sys.argv[2]
	Asset = sys.argv[3]
	Quantity = sys.argv[4]
	
except IndexError:
    print("Needs three arguments (Action Asset Quantity). Ex: python3 exchange.py buy BTC 2")
    exit()
    
if Action.upper() == "BUY":
	price_point = cryptocompare.get_price(Asset, "USD")
	unitPrice = price_point[Asset]["USD"]
	Now = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
	buy(Trader, Asset, Quantity, unitPrice, Now)
	
	
elif Action.upper() == "SELL":
	price_point = cryptocompare.get_price(Asset, "USD")
	unitPrice = price_point[Asset]["USD"]
	Now = datetime.datetime.now().strftime("%Y:%m:%d:%H:%M:%S")
	sell(Trader, Asset, Quantity, unitPrice, Now)

elif Action.upper() == "ASSETS":
	assetFile = open("%s_assets.txt" % Trader, 'r')
	viewAssets(assetFile)
	
elif Action.upper() == "LEDGER":
	ledgerFile = open("%s_ledger.txt" % Trader, 'r')
	viewLedger(ledgerFile)



#get this to the point where you can trade any currency for any other currency
#We also need real time updating of the prive values in the assets file
#can serve as an analysis game for now but will eventually need hooked up to the exchange
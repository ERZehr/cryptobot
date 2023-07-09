#!/usr/bin/python3

#Price Ticker

import datetime # for time
import cryptocompare # for price
import sys # for arguments


Asset = sys.argv[1] # collect first argument
Currency = sys.argv[2] # collect second argument

data = cryptocompare.get_price(Asset, currency=Currency) #fetch price
now = str(datetime.datetime.now()) #fetch time
date = now[slice(10)] #calculate date
time = now[slice(11, 19, 1)] #calculate time
price = str(data[Asset][Currency]) # get price form dictionary

print(date + " " + time + " " + Asset + " " + Currency + " " + str(price))

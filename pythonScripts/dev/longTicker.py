#!/usr/bin/python3
import datetime
import cryptocompare
import sys


def ticker(symbol, currency):

	#initializations
	price_point = cryptocompare.get_price(symbol, currency)
	old_price = price_point[symbol][currency]
	price = 0
	old_time = datetime.datetime.now()
	now = 0
	delta_time = 0
	decimal_delta_time= 0
	delta_price = 0
	old_velocity = 0
	counter = 1	
	
	for n in range(1,20):
		# Get Points and Times 
		price_point = cryptocompare.get_price(symbol, currency)
		price = price_point[symbol][currency]
		now = datetime.datetime.now()
		#rawPoints.write(now.strftime("%Y:%m:%d:%H:%M:%S") + " , " + str(current_price) + '\n')
	
	
		# Velocity/Accel Math
		delta_time = now - old_time
		decimal_delta_time= delta_time.seconds + (delta_time.microseconds * (10 ** -6))
		delta_price = price - old_price
		velocity = delta_price / decimal_delta_time
		acceleration = (velocity - old_velocity) / decimal_delta_time
		#email
		#if condition:
			#send email

	
		print(symbol + "/" + currency + "     Time: " + str(now) + "     Price: %9.8f     Instantaneous Trend: % 9.8f     Acceleration: %9.8f" % (price, velocity, acceleration))
		#comment subsequent 3 for longer scan time trend, uncomment for instantaneous trends
		#old_velocity = velocity
		#old_price = price
		#old_time = now
		counter += 1

#Arguments

try:
	Asset = sys.argv[1]
	Currency = sys.argv[2]
except IndexError:
    print("Needs two arguments (CryptoTicker ReferenceCurrency). Ex: python3 cryptoAI.py BTC USD")
    exit()
    
print('cmd entry:', sys.argv)	
ticker(str(Asset), str(Currency))
	 

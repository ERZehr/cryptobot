#!/bin/bash

#Startup
echo "Enter Trader Name: " 
read trader
echo "Password for "$trader":"
read password
while [ true ]
do
	if [ $password == "amy" ];
		then
		while [ true ]
		do
			echo "Enter Trade: "
			read action security quantity
			python3 exchange.py $trader $action $security $quantity
			if [ $action == "buy" ] || [ $action == "sell" ]
			then
				echo $trader"'s " $action " of " $quantity " " $security " complete"
			fi
		done
	else
		echo "Incorrect"
		echo "Password for "$trader":"
		read password
	fi
done



#only run confirmation line echo if the trade is successful

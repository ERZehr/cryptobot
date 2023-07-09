#!/bin/bash

counter=1

while [ true ]
FILENAME="cryptoLongList.txt"
LINES=$(cat $FILENAME)
do
for LINE in $LINES 
do
	echo $counter
	python3 longTicker.py $LINE USD
	echo -e "\n"
	counter=$((counter+1))
done
counter=1
done

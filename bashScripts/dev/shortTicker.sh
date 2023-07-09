#!/bin/bash


while [ true ]
FILENAME="cryptoShortList.txt"
LINES=$(cat $FILENAME)
do
for LINE in $LINES 
do
	python3 shortTicker.py $LINE USD 
done
done

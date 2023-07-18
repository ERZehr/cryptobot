#!/bin/bash
# COIN CURRENCY POINTS TYPE PERIOD
cd ../../pythonScripts/functional
FILENAME=$(./RSI.py $1 $2 $3 $4 $5)
mv $FILENAME ../../data_files
cd ../../data_files
TIME=$(($3 + $5))
rm ${1}_last_$TIME'_'${4}s

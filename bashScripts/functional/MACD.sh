#!/bin/bash

./EMA.sh $1 $2 12 $(($3 + 1)) $4
./EMA.sh $1 $2 26 $(($3 + 1)) $4
filename12=../../data_files/${1}_12_${4}_EMA_against_last_$(($3 + 1))_${4}s
filename26=../../data_files/${1}_26_${4}_EMA_against_last_$(($3 + 1))_${4}s
python3 ../../pythonScripts/functional/MACD.py $filename12 $filename26 $1 $2 $3 $4
mv ${1}_MACD_last_${3}_${4}s ../../data_files/
rm $filename12
rm $filename26
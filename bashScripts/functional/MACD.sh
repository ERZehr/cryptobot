#!/bin/bash

filename12=$(./EMA.sh $1 $2 12 $3 $4)
filename26=$(./EMA.sh $1 $2 26 $3 $4)
mv $filename12 ../../data_files/
mv $filename26 ../../data_files/
../../pythonScripts/MACD.py
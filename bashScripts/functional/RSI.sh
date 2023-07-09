#!/bin/bash

cd ../../pythonScripts/functional
FILENAME=$(./RSI.py $1 USD $2 $3 $4)
mv $FILENAME ../../data_files
cd ../../data_files
TIME=$(($2 + $4))
rm ${1}_last_$TIME'_'${3}s

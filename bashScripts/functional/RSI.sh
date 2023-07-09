#!/bin/bash

cd ../../pythonScripts/functional
./RSI.py $1 USD $2 $3
cd ../../data_files
rm ${1}_last_${2}_${3}s

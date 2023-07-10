#!/bin/bash

PERIOD=$3
LIMIT=$4
while [ "$PERIOD" -gt "$LIMIT" ]; do
    echo "The data window must be longer than the period."
    read -p "Enter the period: " PERIOD
    read -p "Enter the limit: " LIMIT
done

cd ../../pythonScripts/functional
filename=$(./EMA.py "$1" "$2" "$PERIOD" "$LIMIT" "$5")
mv "$filename" ../../data_files
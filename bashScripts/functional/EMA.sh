#!/bin/bash
cd ../../pythonScripts/functional
filename=$(./EMA.py "$1" "$2" "$3" "$4" "$5")
mv "$filename" ../../data_files
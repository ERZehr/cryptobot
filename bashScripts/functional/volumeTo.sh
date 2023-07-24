#!/bin/bash
cd ../../pythonScripts/functional
filename=$(./volumeTo.py "$1" "$2" "$3" "$4")
mv "$filename" ../../data_files
#!/bin/bash
cd ../../pythonScripts/dev
filename=$(./volumeOscilator.py "$1" "$2" "$3" "$4")
mv "$filename" ../../data_files
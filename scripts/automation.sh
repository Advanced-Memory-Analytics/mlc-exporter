#!/bin/bash

# Run the mlc command and redirect output to temp.txt
./mlc --bandwidth_matrix > temp.txt

# Check to ensure the command was successful
if [ $? -eq 0 ]; then
    echo "Output successfully written to temp.txt"
else
    echo "There was an error running the mlc command."
fi

# Run the parsing script
python3 parseToJSON.py
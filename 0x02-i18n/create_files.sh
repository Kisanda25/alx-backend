#!/bin/bash

# Loop to create multiple files
for i in {0..7}; do
    touch "${i}-app.py"
done

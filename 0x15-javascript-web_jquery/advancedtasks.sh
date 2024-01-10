#!/bin/bash

# Create HTML and JavaScript files for 100 to 103
for i in {100..103}; do
    touch "${i}-main.html"
    touch "${i}-script.js"
done

echo "Files created successfully!"


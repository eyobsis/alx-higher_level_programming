#!/bin/bash

# Create HTML and JavaScript files
for i in {0..9}; do
    touch "${i}-main.html"
    touch "${i}-script.js"
done

# Create README.md
touch README.md

# Populate README.md with content
echo "# JavaScript - Updating HTML Elements" >> README.md
echo "This repository contains JavaScript scripts that demonstrate updating HTML elements." >> README.md
echo "" >> README.md
echo "## Files:" >> README.md
echo "" >> README.md

# List the files and their descriptions in README.md
for i in {0..9}; do
    echo "${i}-main.html: Updates the text or color of an HTML element" >> README.md
    echo "${i}-script.js: JavaScript code for ${i}-main.html" >> README.md
    echo "" >> README.md
done

echo "README.md: Overview of the repository" >> README.md

echo "Files created successfully!"

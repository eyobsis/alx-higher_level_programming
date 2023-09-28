#!/bin/sh

# Define the names of the files to be generated
files=("103-line1.txt" "103-line2.txt" "104-line1.txt" "104-line2.txt" "104-line3.txt" "104-line4.txt" "104-line5.txt" "105-line1.txt" "106-line1.txt" "106-line2.txt" "106-line3.txt" "106-line4.txt" "106-line5.txt")

# Loop over the array of file names and generate each file
for file in ${files[@]}; do
  echo "Generating file $file..."
  touch "$file"
done

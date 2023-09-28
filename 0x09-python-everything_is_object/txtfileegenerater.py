#!/usr/bin/python3

import os

files = [
  "103-line1.txt", 
  "103-line2.txt",
  "104-line1.txt",
  "104-line2.txt", 
  "104-line3.txt",
  "104-line4.txt",
  "104-line5.txt",
  "105-line1.txt",
  "106-line1.txt",
  "106-line2.txt",
  "106-line3.txt", 
  "106-line4.txt",
  "106-line5.txt"
]

for file in files:
  print("Generating file {}".format(file))
  open(file, 'a').close()

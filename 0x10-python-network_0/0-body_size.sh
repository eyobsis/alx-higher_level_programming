#!/bin/bash
# This script takes a URL as an argument, sends a GET request using curl in silent mode,
# and displays the size of the body of the response in bytes.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

body_size=$(curl -sI "$1" | grep -i 'Content-Length' | awk '{print $2}')

echo "$body_size"


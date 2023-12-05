#!/bin/bash
# This script sends a POST request to the URL provided as an argument using curl,
# including the variables email and subject with specific values, and displays the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -X POST -d "email=test@gmail.com" -d "subject=I will always be here for PLD" "$1")
echo "$response"


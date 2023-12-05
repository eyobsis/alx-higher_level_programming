#!/bin/bash
# This script takes a URL as an argument, sends a GET request using curl, and displays the body of the response if the status code is 200.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -o /dev/null -w "%{http_code}" "$1")

if [ "$response" -eq 200 ]; then
    curl -s "$1"
fi


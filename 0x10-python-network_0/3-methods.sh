#!/bin/bash
# This script takes a URL as an argument, sends an OPTIONS request using curl, and displays the allowed HTTP methods.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

allowed_methods=$(curl -sI -X OPTIONS "$1" | grep -i 'Allow' | awk -F ': ' '{print $2}')

echo "$allowed_methods"


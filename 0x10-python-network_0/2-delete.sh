#!/bin/bash
# This script sends a DELETE request to the URL provided as an argument using curl and displays the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -X DELETE "$1")
echo "$response"


#!/bin/bash
# This script sends a GET request to the URL provided as an argument using curl,
# including the header X-School-User-Id with a value of 98, and displays the body of the response.

if [ -z "$1" ]; then
    echo "Usage: $0 <URL>"
    exit 1
fi

response=$(curl -s -H "X-School-User-Id: 98" "$1")
echo "$response"


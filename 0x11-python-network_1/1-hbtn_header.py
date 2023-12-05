#!/usr/bin/python3
"""
Fetches a URL, retrieves the value of the X-Request-Id variable 
from the response header, and displays it.
"""
import urllib.request
import sys

if __name__ == "__main__":
    """
    Fetches a URL, retrieves the value of the X-Request-Id variable 
    from the response header, and displays it.
    """
    with urllib.request.urlopen(sys.argv[1]) as response:
        x_request_id = response.info().get('X-Request-Id')
        print(x_request_id)

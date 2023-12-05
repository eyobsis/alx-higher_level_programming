#!/usr/bin/python3
"""
Takes in a URL and an email, sends a POST request to the passed URL
with the email as a parameter, and displays the body of the
response (decoded in utf-8)
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Takes in a URL and an email, sends a POST request to the passed
    URL with the email as a parameter, and displays the body of the
    response (decoded in utf-8)
    """
    url = argv[1]
    email = argv[2]
    payload = {'email': email}
    response = requests.post(url, data=payload)
    html_str = response.content.decode('utf-8')
    print(html_str)

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
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an HTTPError for unsuccessful status codes
        html_str = response.content.decode('utf-8')
        print(html_str)
    except requests.exceptions.HTTPError as e:
        print("Error code: {}".format(e.response.status_code))

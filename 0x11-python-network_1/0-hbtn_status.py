#!/usr/bin/python3
"""
Fetches https://intranet.hbtn.io/status,
retrieves and displays information about the response body.
"""
import urllib.request

if __name__ == "__main__":
    """
    Fetches https://intranet.hbtn.io/status,
    retrieves and displays information about the response body.
    """
    with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
        html = response.read()
        html_str = html.decode('utf-8')

    print("Body response:")
    print("\t- type: {}".format(type(html)))
    print("\t- content: {}".format(html))
    print("\t- utf8 content: {}".format(html_str))

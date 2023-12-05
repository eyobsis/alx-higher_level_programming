#!/usr/bin/python3
"""
Displays the GitHub user id using the GitHub API with Basic Authentication.
"""
import requests
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    api_url = "https://api.github.com/user"

    response = requests.get(api_url, auth=(username, password))
    if response.status_code == 200:
        user_id = response.json().get('id')
        print(user_id)
    else:
        print(None)

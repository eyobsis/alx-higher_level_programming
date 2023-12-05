"""
Sends a POST request to http://0.0.0.0:5000/search_user with a letter as a parameter.
"""
import requests
from sys import argv

if __name__ == "__main__":
    """
    Takes in a letter and sends a POST request to http://0.0.0.0:5000/search_user with the letter as a parameter.
    """
    endpoint = 'http://0.0.0.0:5000/search_user'
    response = requests.get(endpoint)
    if len(argv) == 2:
        response = requests.post(endpoint, data={'q': argv[1]})
    else:
        response = requests.post(endpoint, data={'q': ""})
    try:
        data = response.json()
        if data == {}:
            print("No result")
        else:
            print("[{}] {}".format(data.get('id'), data.get('name')))
    except ValueError:
        print("Not a valid JSON")

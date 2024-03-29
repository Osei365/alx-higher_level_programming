#!/usr/bin/python3
"""github api"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    r = requests.get('https://api.github.com/user', auth=auth)
    if 'id' in r.json():
        print(r.json()['id'])
    else:
        print(None)

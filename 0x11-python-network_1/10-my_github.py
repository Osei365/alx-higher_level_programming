#!/usr/bin/python3
"""github api"""
import requests
import sys
from requests.auth import HTTPBasicAuth


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    auth = HTTPBasicAuth(username, password)
    r = requests.post('https://api.github.com/user', auth=auth)
    print(r.json()['id'])

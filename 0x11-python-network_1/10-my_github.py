#!/usr/bin/python3
"""github api"""
import requests
import sys


if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    headers = {
            'Accept': 'application/vnd.github+json',
            'Authorization': 'Bearer {}'.format(password),
            'X-GitHub-Api-Version': '2022-11-28'
            }
    r = requests.post('https://api.github.com/user', headers=headers)
    if 'id' in r.json():
        print(r.json()['id'])
    else:
        print(None)

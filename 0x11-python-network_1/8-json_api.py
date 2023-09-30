#!/usr/bin/python3
"""json response content"""
import requests
import sys


if __name__ == "__main__":
    if len(sys.argv) == 1:
        arg = ""
    else:
        arg = sys.argv[1]
    r = requests.post('http://0.0.0.0:5000/search_user', data={'q': arg})
    try:
        ret = r.json()
        if len(ret) == 0:
            print("No result")
        else:
            print("[{}] {}".format(ret.get('id'), ret.get('name')))
    except requests.exceptions.JSONDecodeError:
        print('Not a valid JSON')

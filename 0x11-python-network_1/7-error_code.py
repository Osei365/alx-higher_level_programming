#!/usr/bin/python3
""" handling errors using request."""
import requests
import sys


if __name__ == "__main__":
    url = sys.argv[1]
    r = requests.get(url)
    try:
        r.raise_for_status()
        print(r.text)
    except requests.exceptions.RequestException:
        print("Error code: {}".format(r.status_code))

#!/usr/bin/python3
"""github commits list"""
import requests
import sys


if __name__ == "__main__":
    repo = sys.argv[1]
    owner = sys.argv[2]
    r = requests.get(f'https://api.github.com/repos/{owner}/{repo}/commits')
    for dic in r.json()[:10]:
        auth = dic['commit']['author']['name']
        print("{}: {}".format(dic['sha'], auth))

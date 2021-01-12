#!/usr/bin/python3
""" Get Github """
from sys import argv
import requests


if __name__ == "__main__":
    url, user, token = 'https://api.github.com/user', argv[1], argv[2]
    out = requests.get(url, auth=(user, token))

    try:
        id = (out.json()['id'])
        print(id)
    except KeyError:
        print('None')

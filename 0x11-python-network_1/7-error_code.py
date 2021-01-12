#!/usr/bin/python3
""" Error Code """
from sys import argv
import requests


if __name__ == "__main__":
    url = argv[1]
    out = requests.get(url)
    s_code = out.status_code
    content = out.text

    if s_code >= 400:
        print('Error code: ' + str(s_code))
    else:
        print(content)

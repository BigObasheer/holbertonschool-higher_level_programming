#!/usr/bin/python3
""" Post an email """
from sys import argv
import urllib.request
import urllib.parse



if __name__ == "__main__":
    data = urlib.parse.urlencode({"email": argv[2]}).encode()
    with urlib.request.urlopen(argv[1], data) as f:
        print(f.read().decode('utf-8'))


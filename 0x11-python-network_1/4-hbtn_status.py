#!/usr/bin/python3
"""A DUMB COMMENT"""
import requests


if __name__ == "__main__":
    response = requests.get('https://intranet.hbtn.io/status')
    web = response.text
    print('Body response:')
    print("\t- type: {}".format(type(web)))
    print("\t- content: {}".format(web))

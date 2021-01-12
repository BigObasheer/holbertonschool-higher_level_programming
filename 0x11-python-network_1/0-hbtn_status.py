#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
        with urlib.request.urlopen('https://intranet.hbtn.io/status') as response:
            web = response.read()
            print('Body response:')
            print("\t- type: {}".format(type(page)))
            print("\t- content: {}".format(page))
            print("\t- utf8 content: {}".format(page.decode("UTF-8")))

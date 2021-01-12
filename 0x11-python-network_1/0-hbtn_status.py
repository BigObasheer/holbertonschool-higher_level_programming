#!/usr/bin/python3
""" fetches https://intranet.hbtn.io/status """
import urllib.request


if __name__ == "__main__":
        with urllib.request.urlopen('https://intranet.hbtn.io/status') as response:
            web = response.read()
            print('Body response:')
            print("\t- type: {}".format(type(web)))
            print("\t- content: {}".format(web))
            print("\t- utf8 content: {}".format(web.decode("UTF-8")))

#!/usr/bin/python3
""" sends POST request """
import requests
from sys import argv


if __name__ == "__main__":
    url = 'http://0.0.0.0:5000/search_user'
    if len(argv) is not 2:
        q = ""
    else:
        q = argv[1]
        post = requests.post(url, data={'q': q})
        try:
            data = post.json()
        except:
            print("Not a valid JSON")
        else:
            if data.get("id") is None:
                print("No result")
            else:
                print("[{}] {}".format(data.get("id"), data.get("name")))

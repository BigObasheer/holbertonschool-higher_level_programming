#!/usr/bin/python3
""" Input/Output  """
import json


def load_from_json_file(filename):
    """ save json to a text file """
    with open(filename, "r") as f:
        return json.load(f)

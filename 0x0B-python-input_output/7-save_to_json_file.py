#!/usr/bin/python3
""" Input/Output  """
import json


def save_to_json_file(my_obj, filename):
    """ Writes an Object to a text file """
    with open(filename, mode='w', encoding="utf-8") as new_file:
        json.dump(my_obj, new_file)

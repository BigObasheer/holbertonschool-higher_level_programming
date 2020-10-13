#!/usr/bin/python3
""" Almost a Circle """
from json import dumps as to_json


class Base:
    """ Class Base """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Class Constructor """
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects = Base.__nb_objects + 1
            self.id = Base.__nb_objects

    def to_json_string(li_of_dict):
        return to_json(li_of_dict) if type(li_of_dict) is list else '[]'

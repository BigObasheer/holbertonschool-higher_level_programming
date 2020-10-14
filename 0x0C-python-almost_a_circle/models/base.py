#!/usr/bin/python3
""" Almost a Circle """
from json import dumps as to_json
from json import dump as to_json_file
import json
import csv


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

    @staticmethod
    def to_json_string(li_of_dict):
        """ Converts to JSON """
        return to_json(li_of_dict) if type(li_of_dict) is list else '[]'

    @classmethod
    def save_to_file(cls, list_objs):
        """ Saves to File """
        buff = []
        if buff is not None:
            buff = [x.to_dictionary() for x in list_objs]
            with open(cls.__name__ + ".json", "w") as f:
                f.write(cls.to_json_string(buff))

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

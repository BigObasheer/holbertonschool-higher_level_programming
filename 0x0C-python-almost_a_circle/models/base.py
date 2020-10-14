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
    def save_to_file(cls, list_ob):
        """ Saves to File """
        with open(cls.__name__ + ".json", "w", encoding="utf-8") as f:
            if list_ob is None:
                f.write("[]")
            else:
                f.write(cls.to_json_string([i.to_dictionary() for i
                        in list_ob]))

    @staticmethod
    def from_json_string(json_string):
        """ Returns JSON string representation """
        if json_string is None or json_string == "[]":
            return []
        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """ Create an Instance of the Class """
        if cls.__name__ == "Rectangle":
            ins = cls(1, 1)
        elif cls.__name__ == "Square":
            ins = cls(1)
        else:
            return None
        ins.update(**dictionary)
        return ins

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances """
        try:
            with open(cls.__name__ + ".json", "r") as f:
                buff = f.read()
        except:
            return []
        dicts_list = cls.from_json_string(buff)
        return [cls.create(**inst) for inst in dicts_list]

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ Serializes in CSV """
        filename = cls.__name__ + ".csv"
        s_d = []

        try:
            with open(filename, 'w') as csvfile:
                if list_objs is not None and type(list_objs) is list:
                    if cls.__name__ == "Rectangle":
                        fields = ['id', 'width', 'height', 'x', 'y']
                    elif cls.__name__ == "Square":
                        fields = ['id', 'size', 'x', 'y']

                    for objects in list_objs:
                        s_d.append(objects.to_dictionary())

                    writer = csv.DictWriter(csvfile, fieldnames=fields)
                    writer.writeheader()
                    for dictionaries in s_d:
                        writer.writerow(dictionaries)

                else:
                    with open(filename, 'w') as csvfile:
                        csvfile.write("[]")

        except FileNotFoundError:
            with open(filename, "w") as csvfile:
                csvfile.write("[]")

    @classmethod
    def load_from_file_csv(cls):
        """ Deserializes in CSV """
        filename = cls.__name__ + ".csv"
        instance_list = []

        try:
            with open(filename) as csv_file:
                python_list_of_dictionaries = csv.DictReader(csv_file)

                for elements in python_list_of_dictionaries:
                    for values in elements:
                        elements[values] = int(elements[values])
                    instance_list.append(cls.create(**elements))
                return instance_list

        except FileNotFoundError:
            return []

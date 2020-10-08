#!/usr/bin/python3
""" Input/Output """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """ Return a dict of self """
         if type(attrs) is list and type(attrs[0]) is str:
            return {key: v for key, v in vars(self).items() if key in attrs}
        return vars(self)

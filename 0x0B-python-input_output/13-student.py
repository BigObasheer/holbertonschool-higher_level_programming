#!/usr/bin/python3
""" Input/Output """


class Student:
    def __init__(self, first_name, last_name, age):
        """ Initialize"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self):
        """ Return a dict of self """
        return vars(self)

    def reload_from_json(self, json):
        return None

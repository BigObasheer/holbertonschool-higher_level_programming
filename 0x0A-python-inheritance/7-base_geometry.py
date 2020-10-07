#!/usr/bin/python3
""" Inheritance """


class BaseGeometry:
    """ class BaseGeometry"""
    def integer_validator(self, name, value):
        """ check if positive int """
        if not type(value) is int:
            raise TypeError(str(name) + " must be an integer")
        if value <= 0:
            raise ValueError(str(name) + " must be greater than 0")
    def area(self):
        """ raise Exception """
        raise Exception("area() is not implemented")

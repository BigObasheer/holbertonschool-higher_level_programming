#!/usr/bin/python3
""" Inheritance """


def inherits_from(obj, a_class):
    """ object is an instance of a class that inherited from class """
    return isinstance(obj, a_class) and type(obj) != a_class

#!/usr/bin/python3
""" Inheritance  """


def add_attribute(a, name, other):
    """ try to add a new attribute """
    if hasattr(a, "__dict__"):
        setattr(a, name, value)
    else:
        raise TypeError("can't add new attribute")

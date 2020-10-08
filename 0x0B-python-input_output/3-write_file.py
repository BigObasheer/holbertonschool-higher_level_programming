#!/usr/bin/python3
""" Input/Output """


def write_file(filename="", text=""):
    """ writes a string to a text file and returns the number of chars """
    with open(filename, mode="w", encoding="utf-8") as buffer:
        count = buffer.write(text)
    return count

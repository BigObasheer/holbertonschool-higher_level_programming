#!/usr/bin/python3
""" Input/Output """


def write_file(filename="", text=""):
    """ writes a string to a text file (UTF8) and returns the number of char """
    with open(filename, mode="w", encoding="utf-8") as buffer:
        count = buffer.write(text)
    return count

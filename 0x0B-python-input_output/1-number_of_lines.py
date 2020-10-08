#!/usr/bin/python3
""" Input/Output """


def number_of_lines(filename=""):
    """ returns the number of lines of a text file """
    with open(filename, mode="r", encoding="utf-8") as buffer:
        i = 0
        for lines in buffer:
            i += 1
    return i

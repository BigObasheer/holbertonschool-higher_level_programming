#!/usr/bin/python3
""" Input/Output """


def read_file(filename=""):
    """ reads a text file (UTF8) and prints it to stdout """
    with open(filename, mode="r", encoding="utf-8") as buffer:
        print(buffer.read(), end="")

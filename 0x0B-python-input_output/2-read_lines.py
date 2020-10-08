#!/usr/bin/python3
""" Input/Output """


def read_lines(filename="", nb_lines=0):
    """ reads n lines of a text file (UTF8) and prints it to stdout """
    with open(filename, mode="r", encoding="utf-8") as buffer:
        if nb_lines <= 0:
            print(buffer.read(), end="")

        else:
            i = 0
            for lines in buffer:
                print(lines, end="")
                i += 1
                if i == nb_lines:
                    break

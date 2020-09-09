#!/usr/bin/python3
from sys import argv
if __name__ == "__main__":
    argc = len(argv)
    if argc > 1:
        i = 0
        if argc > 2:
            print("{:d} arguments:".format(argc - 1))
        else:
            print("{:d} argument:".format(argc - 1))
        for arg in argv:
            i += 1
            if i != 1:
                print("{:d}: {}".format(i - 1, arg))
    else:
        print("0 arguments.")
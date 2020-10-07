#!/usr/bin/python3
""" Inheritance """


class MyList(list):
    """class MyList"""
    def print_sorted(self):
        """ print sorted list """
        print(sorted(self))

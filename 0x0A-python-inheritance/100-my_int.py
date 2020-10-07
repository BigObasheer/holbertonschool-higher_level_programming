#!/usr/bin/python3
""" Inheritance """


class MyInt(int):
    """ MyInt is a Rebel """

    def __eq__(self, other):
        """ Equal change to not Equal """
        if isinstance(other, self.__class__):
            return self.__dict__ == other.__dict__
        return False

    def __ne__(self, other):
        """ Change not Equal to Equal """
        return not self.__eq__(other)

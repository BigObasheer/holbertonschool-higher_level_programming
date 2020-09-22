#!/usr/bin/python3
"""Class Square"""


class Square:
    """A square class"""
    __size = None

    def __init__(self, size=0):
        """
        Class Method
        Args:
            self: square
            size: size of the square
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
        Method that returns the area
        """
        return self.__size ** 2

#!/usr/bin/python3y
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

    @property
    def size(self):
        """Method that gets the current size"""
        return self.__size

    @size.setter
    def size(self, value):
        """
        Method that sets the value
        Args:
            self: refers back to the class
            value: value
        """
        if type(value) is not int:
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

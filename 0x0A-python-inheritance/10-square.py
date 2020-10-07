#!/usr/bin/python3
""" Inheritance """
Rectangle = __import__('9-rectangle').Rectangle
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Square(Rectangle):
    """ Class Square """
    def __init__(self, size):
        """ Initialize """
        super().__init__(size, size)
        self.__size = size
        self.integer_validator("size", size)

    def area(self):
        return self.__size * self.__size

#!/usr/bin/python3
""" Inheritance """
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """ class Rectangle"""
    def __init__(self, width, height):
        """ Initialize """
        self.integer_validator("width", width)
        self.integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ Area """
        return self.__width * self.__height

    def __str__(self):
        """ String """
        string = "[Rectangle] " + str(self.__width) + "/" + str(self.__height)
        return string

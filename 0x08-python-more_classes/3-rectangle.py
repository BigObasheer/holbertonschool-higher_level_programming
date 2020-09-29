#!/usr/bin/python3
""" Defines the Rectangle class """


class Rectangle:
    """ Defines a rectangle with a width and height value
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """ Defines width of rectangle
            width must be an int and above 0
        """
        return self.__width

    @width.setter
    def width(self, value):
        if type(value) != int:
            raise TypeError('width must be an integer')

        if value < 0:
            raise ValueError('width must be >= 0')

        self.__width = value

    @property
    def height(self):
        """ Defines height of rectangle
            height must be an int and above 0
        """
        return self.__height

    @height.setter
    def height(self, value):
        if type(value) != int:
            raise TypeError('height must be an integer')

        if value < 0:
            raise ValueError('height must be >= 0')

        self.__height = value

    def area(self):
        """ returns the rectangle area """
        return self.__height * self.__width

    def perimeter(self):
        """ returns the rectangle perimeter """
         """ Perimeter of rectangle """
        if self.__height is 0 or self.__width is 0:
            return 0
        return (self.__width * 2) + (self.__height * 2)

    def __str__(self):
        """ Str representation of rectangle """
        new = ""
        if self.__width is 0 or self.__height is 0:
            return new
        for i in range(self.__height):
            new += (("#" * self.__width) + "\n")
        return new[:-1]

#!/usr/bin/python3
""" Defines the Rectangle class """


class Rectangle:
    """ Defines a rectangle with a width and height value
    Args:
        width (int): width of rectangle
        height (int): height of rectangle
    """

    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """ Defines width of rectangle.
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
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__width + self.__height)

    def __str__(self):
        """ returns string representation of class """
        str = ""
        if self.width == 0 or self.height == 0:
            str += "\n"
            return ""
        else:
            for i in range(self.height):
                str += "#" * self.width
                if i < self.height - 1:
                    str += "\n"
            return str

    def __repr__(self):
        """
        print string representing width and height of rectangle
        """
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        """
        deletes rectangle
        """
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
        del self

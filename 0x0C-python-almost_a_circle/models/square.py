#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize """
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        """ Returns Size Value """
        return self.width

    @size.setter
    def size(self, value):
        """ Sets Size Value """
        self.width = value
        self.height = value

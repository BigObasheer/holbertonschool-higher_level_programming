#!/usr/bin/python3
""" Class Square """
from models.rectangle import Rectangle


class Square(Rectangle):
    """ Class Square that inherits from Rectangle """
    def __init__(self, size, x=0, y=0, id=None):
        """ Initialize """
        self.size = size
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

    def __str__(self):
        """ String Method """
        s = "[Square] ({}) {}/{} - {}"
        s = s.format(self.id, self.x, self.y, self.size)
        return s

    def update(self, *args, **kwargs):
        """ Update """
        if args:
            attrs = ['id', 'size', 'x', 'y']
            for index in range(len(args)):
                setattr(self, attrs[index], args[index])
        else:
            for k, v in kwargs.items():
                setattr(self, k, v)

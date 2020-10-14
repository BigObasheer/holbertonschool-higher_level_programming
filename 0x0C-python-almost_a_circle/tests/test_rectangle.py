!/usr/bin/python3
""" Unit Test """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestRectangle(unittest.TestCase):
    """ Test for class Rectangle """

    def test_rec_init(self):
        r1 = Rectangle(10, 2)
        self.assertEqual(r1.id, 5)
        r2 = Rectangle(2, 10)
        self.assertEqual(r2.id, 6)
        r3 = Rectangle(10, 2, 0, 0, 15)
        self.assertEqual(r3.id, 15)
        with self.assertRaises(TypeError):
            Rectangle(10, 2, 3, 4, 5, 5)

    def test_largeArea(self):
        r = Rectangle(5000000, 100000000, 2, 10, 1)
        self.assertEqual(500000000000000, r.area())

    def test_1argArea(self):
        r = Rectangle(5, 8, 1, 1, 1)
        with self.assertRaises(TypeError):
            r.area(1)

    def test_pep8(self):
        """ Test prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/rectangle.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")

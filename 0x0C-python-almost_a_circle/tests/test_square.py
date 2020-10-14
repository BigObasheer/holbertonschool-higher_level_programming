#!/usr/bin/python3
""" Unit Test """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class TestSquare(unittest.TestCase):
    """ Test for class square """
    def test_area(self):
        s1 = Square(5)
        self.assertEqual(s1.area(), 25)

    def test_less_than_zero(self):
        """Test for zero and neg inputs"""
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(-1)
        with self.assertRaisesRegex(ValueError, "width must be > 0"):
            Square(0)
        with self.assertRaisesRegex(ValueError, "x must be >= 0"):
            Square(1, -4)
        with self.assertRaisesRegex(ValueError, "y must be >= 0"):
            Square(1, 5, -2)

    def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/square.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")

#!/usr/bin/python3
""" Unit Test """
import unittest
from models.base import Base
from models.rectangle import Rectangle
from models.square import Square
import pep8


class test_Base(unittest.TestCase):
    """ Tests for class Base """
    def test_default(self):
        b = Base()
        self.assertEqual(b.id, 1)

    def test_manyArgs_id(self):
        with self.assertRaises(TypeError):
            b = Base(1, 1)

    def test_neg_id(self):
        self.assertEqual(-5, Base(-5).id)

    def test_zero_id(self):
        self.assertEqual(0, Base(0).id)

    def test_float_id(self):
        self.assertEqual(1.5, Base(1.5).id)

    def test_str_id(self):
        self.assertEqual("hello", Base("hello").id)

    def test_list_id(self):
        self.assertEqual([1, 2, 3], Base([1, 2, 3]).id)

    def test_tuple_id(self):
        self.assertEqual((1, 2), Base((1, 2)).id)

    def test_set_id(self):
        self.assertEqual({1, 2, 3}, Base({1, 2, 3}).id)

    def test_dict_id(self):
        self.assertEqual({"a": 1, "b": 2}, Base({"a": 1, "b": 2}).id)

    def test_noneDict(self):
        b = Base()
        self.assertEqual(b.to_json_string(None), "[]")

    def test_reg_dict_to_string(self):
        b = Base()
        tmp = {"id": 1, "width": 10, "height": 2, "x": 1, "y": 9}
        self.assertEqual(type(b.to_json_string(tmp)), str)

     def test_pep8(self):
        """ tests prp8 formating """
        pep8style = pep8.StyleGuide(quiet=True)
        result = pep8style.check_files(['models/base.py'])
        self.assertEqual(result.total_errors, 0,
                         "Found code style erros (and warnings).")

if __name__ == "__main__":
    unittest.main()

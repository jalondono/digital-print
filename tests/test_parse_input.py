import contextlib
import unittest
from io import StringIO

from src.parse_input import verify_input
from src.parse_input import str2list


class TestVerifyInput(unittest.TestCase):
    # Verify_input function
    def test_spaces(self):
        # test more than 2 arguments
        self.assertRaises(ValueError, verify_input, '3,154 0,0 66')

    def test_negative_values(self):
        # Test negative values un input
        self.assertRaises(ValueError, verify_input, '-3,154 0,0')

    def test_blank_spaces(self):
        # test blank spaces in the input
        self.assertRaises(ValueError, verify_input, ' -3,154    0,0 ')

    def test_dot_instead_comas(self):
        # test the input with dots instead comas
        self.assertRaises(ValueError, verify_input, '3.154 0.0')


class Str2List(unittest.TestCase):
    # Verify_input function
    def test_convert(self):
        # test conversion str to list
        self.assertEqual(['3', '154', '0,0'], str2list('3,154 0,0'))

    def test_one_parameter(self):
        # convert just one parameter
        self.assertEqual(['3', '154'], str2list('3,154'))

    def test_convert_parameter_spaces(self):
        # convert just one parameter
        self.assertEqual(['3', '154'], str2list('   3,154 '))

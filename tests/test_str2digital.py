import contextlib
import unittest
from io import StringIO
import numpy as np

from src.str2digital import get_segment_setup
from src.str2digital import print_matrix
from src.str2digital import convert2integers
from src.str2digital import transform_numbers


class TestGetSegmentSetup(unittest.TestCase):
    def test_get_setup(self):
        # Test to get a setup of a segment given a number
        self.assertEqual({'a': 1, 'b': 1, 'c': 1, 'd': 0, 'e': 1, 'f': 1, 'g': 1}, get_segment_setup(0))


class TestConvert2Integers(unittest.TestCase):
    def test_convert(self):
        # test convert a str list into a integer list
        self.assertEqual([1, 123], (convert2integers(['1', '123'])))


class TestPrintMatrix(unittest.TestCase):
    # test to print a digit
    def test_print_matrix(self):
        # print a np.array
        array = np.array([[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
                 [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]])
        inp = '          \n      |   \n          \n      |   \n          \n      |   \n\
          \n\
          \n\
          \n\
      |   \n\
          \n\
      |   \n\
          \n\
      |   \n\
          \n'

        temp_stdout = StringIO()
        with contextlib.redirect_stdout(temp_stdout):
            print_matrix(array)
        output = temp_stdout.getvalue()

        self.assertMultiLineEqual(inp, output)

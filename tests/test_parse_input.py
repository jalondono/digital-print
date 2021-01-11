import contextlib
import unittest
from io import StringIO

from src.parse_input import verify_input
from src.parse_input import str2list


class TestParseInput(unittest.TestCase):
    def test_spaces(self):
        # test more than 2 arguments
        self.assertRaises(ValueError, verify_input, '3,154 0,0 66')

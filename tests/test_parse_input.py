import contextlib
import unittest
from io import StringIO

from src.parse_input import verify_input
from src.parse_input import str2list


class TestVerifyInput(unittest.TestCase):
    # Verify_input function
    def test_spaces(self):
        # test more than 2 arguments
        temp_stdout = StringIO()
        inp = 'The format input is incorrect, Should be as follow: \n <size>,<number>\n'
        with contextlib.redirect_stdout(temp_stdout):
            verify_input('3,154 0,0 66')
        output = temp_stdout.getvalue()

        self.assertMultiLineEqual(inp, output)

    def test_negative_values(self):
        # Test negative values un input
        temp_stdout = StringIO()
        inp = 'The format input is incorrect, Should be as follow: \n <size>,<number>\n'
        with contextlib.redirect_stdout(temp_stdout):
            verify_input('-3,154 0,0')
        output = temp_stdout.getvalue()

        self.assertMultiLineEqual(inp, output)

    def test_blank_spaces(self):
        # test blank spaces in the input
        temp_stdout = StringIO()
        inp = 'The format input is incorrect, Should be as follow: \n <size>,<number>\n'
        with contextlib.redirect_stdout(temp_stdout):
            verify_input(' -3,154    0,0 ')
        output = temp_stdout.getvalue()

        self.assertMultiLineEqual(inp, output)

    def test_dot_instead_comas(self):
        # test the input with dots instead comas
        temp_stdout = StringIO()
        inp = 'The format input is incorrect, Should be as follow: \n <size>,<number>\n'
        with contextlib.redirect_stdout(temp_stdout):
            verify_input('3.154 0.0')
        output = temp_stdout.getvalue()

        self.assertMultiLineEqual(inp, output)


class TestStr2List(unittest.TestCase):
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

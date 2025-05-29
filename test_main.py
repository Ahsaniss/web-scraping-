# Import the square_number function from main.py
from refactor3 import square_number  # Make sure 'main' matches the name of your Python file containing the function

import unittest


class TestSquareNumber(unittest.TestCase):

    # Positive Test Case 1: Test with a positive integer
    def test_square_positive_integer(self):
        self.assertEqual(square_number(4), 16)

    # Positive Test Case 2: Test with a float
    def test_square_float(self):
        self.assertEqual(square_number(2.5), 6.25)

    # Negative Test Case 1: Test with a string input
    def test_square_string(self):
        with self.assertRaises(ValueError):
            square_number("string")

    # Negative Test Case 2: Test with None input
    def test_square_none(self):
        with self.assertRaises(ValueError):
            square_number(None)


if __name__ == '__main__':
    unittest.main()

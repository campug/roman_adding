#! /usr/bin/env python3

"""The unit tests for roman_adding.py and its add() function.

Although I prefer pytest, we use unittest because it is part of the Python3
standard library.
"""

import unittest

from roman_adding import add


class TestRomanAdding(unittest.TestCase):
    """Test adding roman numbers.
    """

    def test_not_roman_arg1(self):
        with self.assertRaisesRegex(ValueError, "'i' is not .*"):
            add('i', 'I')

    def test_not_roman_arg2(self):
        with self.assertRaisesRegex(ValueError, "'i' is not .*"):
            add('I', 'i')

    def test_add_I_I(self):
        self.assertEqual(add('I', 'I'), 'II')

    def test_add_II_I(self):
        self.assertEqual(add('II', 'I'), 'III')

    def test_add_III_I(self):
        self.assertEqual(add('III', 'I'), 'IV')


if __name__ == '__main__':
    unittest.main()

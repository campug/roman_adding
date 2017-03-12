#! /usr/bin/env python3

"""The unit tests for roman_adding.py and its add() function.

Although I prefer pytest, we use unittest because it is part of the Python3
standard library.
"""

import unittest

# Rather than write my own, let's use someone else's function to
# convert to roman numbers
from to_roman import to_roman

from roman_adding import add


class TestRomanAdding(unittest.TestCase):
    """Test adding roman numbers.

    This is the "old fashioned" way of using unittests for doing many tests
    - as you can see, those test_add_<a>_<b> methods would get tedious very
    quickly.
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


class TestRomanAddingSubTests(unittest.TestCase):
    """Test adding roman numbers.

    From Python 3.4, unittest adds the ability to add sub tests, which will
    report all the failures in a loop, without stopping at the first one.
    This may be more convenient.
    """

    def test_adding(self):

        for a in range(1, 2):
            for b in range(1, 2):
                ar = to_roman(a)
                br = to_roman(b)
                with self.subTest(ar=ar, br=br):
                    self.assertEqual(add(ar, br), to_roman(a+b))


if __name__ == '__main__':
    unittest.main()

#! /usr/bin/env python3

"""Support for adding two roman numbers.

The idea is to write a function, add, that takes two strings as arguments,
each of which is a roman number. The function returns the sum of the two
arguments, also as a string representing a roman number. Ideally, this is
done only using string operations, without any use of "normal" numbers.

The rules for representing roman numbers are (stealing liberally from
https://en.wikipedia.org/wiki/Roman_numerals):

* The numerals are: I (1), V (5), X (10), L (50), C (100), D (500), M (1000)
* Numbers above 3000 are not supported (so you don't need to worry about
  inputs *or outputs* above that amount) - although it's OK if they do work.
* Generally, numbers are formed by adding adjacent values - so

  * CCVII is 100 + 100 + 5 + 1 + 1 which is 207, and
  * MLXVI is 1000 + 50 + 10 + 1, which is 1066,

* In special cases, four repeating characters are instead always replaced by 
  "subtractive notation", e.g., IV means 4, instead of IIII.

  * So we have IV (4), IX (9), XL (40), XC (90), CD (400), CM (900)
  * The rule is that a numeral may be placed before either of the next two
    larger digits. This means you are not allowed represent 49 as IL (1 less
    than 50), but must instead do XLIX (40 + 9).
  * Other examples are MCMIV (1000 + 900 + 4) for 1904,
    MCMLIV (1000 + 900 + 50 + 4) for 1954 and
    MCMXC (1000 + 900 + 90) for 1990

Output should always be in these tidy forms.

I believe it is possible to do addition of these forms entirely with string
operations.

If you want to be extra clever, after you've got that working, you can try
to also allow a more "relaxed" form of input, where the restriction on always
turning four repeated sybmols into the substractive form is relaxed - so for
instance, allowing IIII as well as IV, and even XXXXXX instead of LX.
(Although it's possible that it might just work...)
"""

import sys

ROMAN_DIGITS = 'IVXLCDM'

def check_roman(s):
    """If 's' is not a roman number, raise a Value Error.
    """
    if not all(x in ROMAN_DIGITS for x in s):
        raise ValueError('{!r} is not a sequence of I, V, X, L, C, D or M'.format(s))

class RomanAdder(object):

    def __init__(self):
        self.clear()

    def clear(self):
        """Clear our internal accumulators.
        """
        self.accum_i = ''
        self.accum_v = ''
        self.accum_x = ''
        self.accum_l = ''
        self.accum_c = ''
        self.accum_d = ''
        self.accum_m = ''

        self.accum_iv = ''
        self.accum_ix = ''
        self.accum_xl = ''
        self.accum_xc = ''
        self.accum_cd = ''
        self.accum_cm = ''

    def split(self, number):
        """Split a roman number up into it parts.

        Raises ValueError if 'number' contain any characters other than
        "I", "V", "X", "L", "C", "D" or "M".
        """
        check_roman(number)
        while number.endswith('I'):
            number = number[:-1]
            self.accum_i += 'I'

        if number.endswith('IV'):
            number = number[:-2]
            self.accum_i += 'IIII'
        while number.endswith('V'):
            number = number[:-1]
            self.accum_v += 'V'

        if number.endswith('IX'):
            number = number[:-2]
            self.accum_i += 'IIII'
            self.accum_v += 'V'
        while number.endswith('X'):
            number = number[:-1]
            self.accum_x += 'X'

        if number.endswith('XL'):
            number = number[:-2]
            self.accum_x += 'XXXX'
        while number.endswith('L'):
            number = number[:-1]
            self.accum_l += 'L'

        if number.endswith('XC'):
            number = number[:-2]
            self.accum_x += 'XXXX'
            self.accum_l += 'L'
        while number.endswith('C'):
            number = number[:-1]
            self.accum_c += 'C'

        if number.endswith('CD'):
            number = number[:-2]
            self.accum_c += 'CCCC'
        while number.endswith('D'):
            number = number[:-1]
            self.accum_d += 'D'

        if number.endswith('CM'):
            number = number[:-2]
            self.accum_c += 'CCCC'
            self.accum_d += 'D'
        while number.endswith('M'):
            number = number[:-1]
            self.accum_m += 'M'

    def add(self, number1, number2):
        """Add two strings representing roman numbers.

        For instance:

          >>> adder = RomanAdder()
          >>> adder.add('IV', 'V')
          'IX'

        Raises ValueError if the strings contain any characters other than
        'I', 'V', 'X', 'L', 'C', 'D' or 'M'.
        """
        self.clear()
        self.split(number1)
        self.split(number2)

        # Simple accumulations
        while self.accum_i.endswith('IIIII'):
            self.accum_i = self.accum_i[:-5]
            self.accum_v += 'V'

        while self.accum_v.endswith('VV'):
            self.accum_v = self.accum_v[:-2]
            self.accum_x += 'X'

        while self.accum_x.endswith('XXXXX'):
            self.accum_x = self.accum_x[:-5]
            self.accum_l += 'L'

        while self.accum_l.endswith('LL'):
            self.accum_l = self.accum_l[:-2]
            self.accum_c += 'C'

        while self.accum_c.endswith('CCCCC'):
            self.accum_c = self.accum_c[:-5]
            self.accum_d += 'D'

        while self.accum_d.endswith('DD'):
            self.accum_d = self.accum_d[:-2]
            self.accum_m += 'M'

        # Subtractive values from two accumulators
        if self.accum_v == 'V' and self.accum_i == 'IIII':
            self.accum_ix = 'IX'
            self.accum_v  = ''
            self.accum_i  = ''

        if self.accum_l == 'L' and self.accum_x == 'XXXX':
            self.accum_xc = 'XC'
            self.accum_l  = ''
            self.accum_x  = ''

        if self.accum_d == 'D' and self.accum_c == 'CCCC':
            self.accum_cm = 'CM'
            self.accum_d  = ''
            self.accum_c  = ''

        # Subtractive values from a single accumulator
        if self.accum_i == 'IIII':
            self.accum_iv = 'IV'
            self.accum_i = ''

        if self.accum_x == 'XXXX':
            self.accum_xl = 'XL'
            self.accum_x = ''

        if self.accum_c == 'CCCC':
            self.accum_cd = 'CD'
            self.accum_c = ''

        sum = (self.accum_m + self.accum_cm +
               self.accum_d + self.accum_cd +
               self.accum_c + self.accum_xc +
               self.accum_l + self.accum_xl +
               self.accum_x + self.accum_ix +
               self.accum_v + self.accum_iv +
               self.accum_i)

        return sum


def add(number1, number2):
    """Add two strings representing roman numbers.

    For instance:

      >>> add('IV', 'V')
      'IX'

    Raises ValueError if the strings contain any characters other than
    'I', 'V', 'X', 'L', 'C', 'D' or 'M'.
    """
    adder = RomanAdder()
    return adder.add(number1, number2)



def main(args):
    """Allow adding things from the command line.
    """
    if len(args) != 2:
        print('Usage: roman_adding.py <roman-number1> <roman-number2>')
    print(add(args[0], args[1]))

if __name__ == '__main__':
    main(sys.argv[1:])

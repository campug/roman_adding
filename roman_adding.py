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
from itertools import groupby
from collections import OrderedDict

# digits here must be in ascending order
ROMAN_DIGITS = 'IVXLCDM'

# use ordered dict as replace_additive must be done starting from largest digits
ADDITIVE_MAP = OrderedDict()
ADDITIVE_MAP['CM']='DCCCC'
ADDITIVE_MAP['CD']='CCCC'
ADDITIVE_MAP['XC']='LXXXX'
ADDITIVE_MAP['XL']='XXXX'
ADDITIVE_MAP['IX']='VIIII'
ADDITIVE_MAP['IV']='IIII'

# order here is not critical, so just using a regular dictionary
REDUCTION_MAP = {}
REDUCTION_MAP['IIIII']='V'
REDUCTION_MAP['VIV']='IX'
REDUCTION_MAP['VV']='X'
REDUCTION_MAP['XXXXX']='L'
REDUCTION_MAP['LXL']='XC'
REDUCTION_MAP['LL']='C'
REDUCTION_MAP['CCCCC']='D'
REDUCTION_MAP['DCD']='CM'
REDUCTION_MAP['DD']='M'


def check_roman(s):
    """If 's' is not a roman number, raise a Value Error.
    """
    if not all(x in ROMAN_DIGITS for x in s):
        raise ValueError('{!r} is not a sequence of I, V, X, L, C, D or M'.format(s))

def replace_subtractive(number):
    """ replace subtractive number components with additive format equivalent
    so digit order becomes unimportant"""
    for sub,add in ADDITIVE_MAP.items():
        if sub in number:
            number = number.replace(sub,add)
    return number

def replace_additive(number):
    """ where a digit series can be shortened, replace with standard subtractive
    format equivalent"""
    for key, value in ADDITIVE_MAP.items():
        if value in number:
            number = number.replace(value, key)
    return number

def fold_digits(number):
    """ where a digit series can be replaced by next digit up, do so """
    for digits, reduction in REDUCTION_MAP.items():
        if digits in number:
            number = number.replace(digits, reduction)
    return number

def add(number1, number2):
    """Add two strings representing roman numbers.

    For instance:

      >>> add('IV', 'V')
      'IX'

    Raises ValueError if the strings contain any characters other than
    'I', 'V', 'X', 'L', 'C', 'D' or 'M'
    """
    check_roman(number1)
    check_roman(number2)

    # replace subtractive numbers such as IV with additive version such as IIII
    number1 = replace_subtractive(number1)
    number2 = replace_subtractive(number2)

    # concatenate strings then sort digits into descending order
    sum = number1 + number2
    sum = ''.join(sorted(sum, key=lambda x: ROMAN_DIGITS.index(x), reverse=True))

    # replace digit series such as XXXX with higher digit equivalent such as L
    # where possible till no further change is possible
    while sum != fold_digits(sum):
        sum = fold_digits(sum)

    # where additive strings such as IIII can be replaced with subtractive
    # equivalent such as IV, do so
    sum = replace_additive(sum)

    return sum


def main(args):
    """Allow adding things from the command line.
    """
    if len(args) != 2:
        print('Usage: roman_adding.py <roman-number1> <roman-number2>')
    print(add(args[0], args[1]))

if __name__ == '__main__':
    main(sys.argv[1:])

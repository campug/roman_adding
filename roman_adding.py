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


def add(number1, number2):
    """Add two strings representing roman numbers.

    For instance:

      >>> add('iv', 'v')
      'ix'

    """
    return number1 + number2


def main(args):
    """Allow adding things from the command line.
    """
    if len(args) != 2:
        print('Usage: roman_adding.py <roman-number1> <roman-number2>')
    print(add(args[0], args[1]))

if __name__ == '__main__':
    main(sys.argv[1:])

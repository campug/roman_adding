#! /usr/bin/env python3

"""A very simple function for converting an integer to roman numerals.
"""

import sys

int_to_roman = (
    (1000, 'M'),
    (900,  'CM'),
    (500,  'D'),
    (400,  'CD'),
    (100,  'C'),
    (90,   'XC'),
    (50,   'L'),
    (40,   'XL'),
    (10,   'X'),
    (9,    'IX'),
    (5,    'V'),
    (4,    'IV'),
    (1,    'I'),
)


def to_roman(number):
    """Given an integer, return a roman number.

    Somewhat arbitrarily, we assume that Romans never counted above 3000,
    so that's the highest number we support.
    """
    if not isinstance(number, int):
        raise ValueError('{!r} is not an integer'.format(number))
    if number < 1:
        raise ValueError('Roman numbers do not allow zero or less, so not {}'.format(number))
    if number > 3000:
        raise ValueError('We do not support {}, it is more than 3000'.format(number))
    result = ''
    for integer, part in int_to_roman:
        while number >= integer:
            result += part
            number -= integer
    return result


if __name__ == '__main__':
    args = sys.argv[1:]
    if len(args) != 1:
        print(__doc__)
        sys.exit(1)
    try:
        number = int(args[0], 10)
    except ValueError as e:
        print(e)
        sys.exit(1)
    print(to_roman(number))

Roman adding kata
=================
This is a simple Python kata about adding Roman numbers using string operations.

It is inspired by the description at http://codingdojo.org/kata/RomanCalculator/

It is being used at CamPUG (the Cambridge Python User Group) on Tuesday 7th
March 2017 - see us on meetup.com at https://www.meetup.com/CamPUG/

See the docstring at the top of roman_adding.py for the aim of the kata,
and see test_roman_adding.py for the unit tests.

Tibs's solution
---------------
This was the simplest possible solution I could think of. Clearly it's also
very inefficient, as there's lots of adding of strings. Using lists would
presumably be faster. For adding two roman numbers together, that doesn't
really matter, but it does make the unit tests really slow when testing
over a large range.

After writing it, it became obvious that this is really equivalent to putting
the I, X, etc., values from both input numbers onto some sort of abacus, and
then reading the result off again.

It was also pointed out to me that I could sensibly have used a dictionary
to hold the tallies, instead of individual variables, which is definitely
true, and that doing that would have meant I didn't need the class, which
would arguably be a lot simpler.

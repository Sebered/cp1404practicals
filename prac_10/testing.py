"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_06.car import Car


def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)


def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # the test below should fail
    assert repeat_string("hi", 2) == "hi hi"

    # assert test with custom message,
    # used to see if Car's init method sets the odometer correctly
    # this should pass (no output)
    car = Car(name = "test1")
    assert car._odometer == 0, "Car does not set odometer correctly"

    assert car.fuel == 0, "Car does not set the default fuel value correctly"

    # Note that Car's __init__ function sets the fuel in one of two ways:
    # using the value passed in or the default
    # You should test both of these
    car = Car(name = "test2", fuel = 10)
    assert car.fuel == 10, "Car does not set the custom fuel value correctly"


run_tests()

# (PyCharm may see your >>> doctest comments and run doctests anyway.)
doctest.testmod()

# (Don't change the tests, change the function!)

# TODO: 5. Write and test a function to format a phrase as a sentence,
# starting with a capital and ending with a single full stop.
# Important: start with a function header and just use pass as the body
# then add doctests for 3 tests:
#   'hello' -> 'Hello.'
#   'It is an ex parrot.' -> 'It is an ex parrot.'
# and one more that you decide is a useful test.
# Run your doctests and watch the tests fail.
# Then write the body of the function so that the tests pass.

def format_as_sentence(phrase):
    """
    >>> format_as_sentence("hello world")
    'Hello world.'
    >>> format_as_sentence("Python has so many fancy features.")
    'Python has so many fancy features.'
    >>> format_as_sentence("howdy, how is the family")
    'Howdy, how is the family.'
    """
    phrase = phrase.strip()
    if not phrase:
        return ""

    formatted = phrase[0].upper() + phrase[1:]
    if not formatted.endswith("."):
        formatted += "."

    return formatted
"""Coding examples with string in python."""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


def first_nonrepreated_character(string):
    """return first non repeated character in string.

    Example::
    >>> first_nonrepreated_character("foo")
    f
    """
    d = {}
    for char in string:
        seen = d.get(char)
        if seen is None:
            d[char] = "once"
        elif seen is "once":
            d[char] = "multiple"
        else:
            pass
    for char in string:
        if d[char] is "once":
            return char


def str2int(string):
    """convert a string representing a number to an int.

    Example:
    >>> str2int("42")
    42
    """
    sum = 0
    multiplier = 1
    for i in xrange(len(string)-1, -1, -1):
        sum += int(string[i]) * multiplier
        multiplier *= 10
    return sum


def int2str(num):
    """convert a integer to string representing the number.

    Example:
    >>> int2str(42)
    "42"
    """
    string = ""
    while num > 0:
        string = str(num % 10) + string
        num /= 10
    return string

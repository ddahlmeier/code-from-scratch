"""Recursion coding examples in python."""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


def fact(n):
    """Factorial of n

    Example:
    >>> fact(3)
    6
    """
    if n == 1:
        return 1
    else:
        return n * fact(n-1)


def permutations(string):
    """print all permuations of the characters in string

    Example:
    >>> permutations("fo")
    fo
    of
    """
    permute(string, '')


def permute(string, out):
    """helper method to find  all permuations """
    if len(string) == 0:
        print out
    else:
        for i in xrange(len(string)):
            permute(string[:i] + string[i+1:], out + string[i])


def combinations(string):
    """print all combinations of the characters in string

    Example:
    >>> combinations("fo")

    f
    o
    fo
    """
    combine(string, '')


def combine(string, out=''):
    """helper method to find  all combinations """
    if len(string) == 0:
        # base case
        if out:
            print out
    else:
        # recurison casse
        combine(string[1:], out)
        combine(string[1:], out+string[0])


def telephone_words(number, word=''):
    "print all words for a telphone number using the dial pad encoding"""
    digit2char = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'],
                  '4': ['g', 'h', 'i'], '5': ['j', 'k', 'l'],
                  '6': ['m', 'n', 'o'], '7': ['p', 'r', 's'],
                  '8': ['t', 'u', 'v'], '9': ['w', 'x', 'y']}
    if len(number) == 0:
        print word
    else:
        for char in digit2char[number[0]]:
            telephone_words(number[1:], word + char)

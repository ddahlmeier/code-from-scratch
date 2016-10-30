"""Arrays and Strings examples from Cracking the coding interview Chapter 1"""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


from collections import Counter
import numpy as np


def uniq(iter):
    """return unique elements in iter"""
    return {item: 1 for item in iter}.keys()


def is_unique(string):
    """determine if the string has all unique characters"""
    return uniq(Counter(string).values()) == [1]


def check_permutation(left, right):
    """determine if one string is permuation of the other"""
    if len(left) != len(right):
        return False
    return Counter(left) == Counter(right)


def palindrome_permutation(string):
    """determine if string is permuation of a palindrome"""
    # character counts need to be even, optional there is a single
    # character with odd count
    return Counter(map(lambda x: x % 2, Counter(string).values()))[1] in [0, 1]


def edit_dist(left, right):
    """compute edit distance between two strings"""
    grid = [[0 for i in xrange(len(right)+1)] for j in xrange(len(left)+1)]
    # initialize first rown and column
    for row in xrange(len(left)+1):
        grid[row][0] = row
    for col in xrange(len(right)+1):
        grid[0][col] = col
    # dynamic programming
    for row in xrange(1, len(left)+1):
        for col in xrange(1, len(right)+1):
            if left[row-1] == right[col-1]:
                grid[row][col] = min(grid[row-1][col-1], grid[row][col-1]+1,
                                     grid[row-1][col]+1)
            else:
                grid[row][col] = min(grid[row-1][col-1]+1, grid[row][col-1]+1,
                                     grid[row-1][col]+1)
    return grid[-1][-1]


def one_away(first, second):
    """determine if strings are at most one edit distance away"""
    def one_away_repl(first, second):
        return sum(int(c != d) for c, d in zip(first, second)) <= 1

    def one_away_insert(first, second):
        return any(first[:i] + second[i] + first[i:]
                   for i in xrange(len(second)))

    if len(first) == len(second):
        return one_away_repl(first, second)
    elif len(first) == len(second)+1:
        return one_away_insert(first, second)
    elif len(first)+1 == len(second):
        return one_away_insert(first, second)
    else:
        return False


def string_compr(string):
    """ simple string compression using length encoding"""
    count = 0
    out = []
    if len(string) < 2:
        return string
    
    for last, next in zip(string, string[1:]):
        count += 1
        if last != next:
            out.append((last, count))
            count = 0
    # handle last character
    if last == next:
        out.append((last, count+1))
    else:
        out.append((next,1))
    compr =  "".join(["%s%d" % (char, count) for char, count in out])
    return compr if len(compr) < len(string) else string


def rotate_matrix(matrix):
    """rotate matrix by 90 degrees in place"""
    n = matrix.shape[0]
    for i in xrange(n//2):
        for j in xrange(n//2):
            matrix[i, n-j-1], matrix[n-i-1, n-j-1], matrix[n-i-1, j], \
                matrix[i, j], = matrix[i, j], matrix[i, n-j-1], \
                matrix[n-i-1, n-j-1], matrix[n-i-1, j ]
    return matrix


def zero_matrix(matrix):
    """zero rown and column for every zero entry"""
    n, m = matrix.shape
    out = matrix.copy()
    for i in xrange(n):
        for j in xrange(m):
            if matrix[i, j] == 0:
                for k in xrange(n):
                    out[k, j] = 0
                for k in xrange(m):
                    out[i, k] = 0
    return out

if __name__ == "__main__":
    print "1.1 Is Unique"
    print "  is_unique('bar') = ", is_unique('bar')
    print "  is_unique('foo') = ", is_unique('foo')

    print "1.2 Check Permutatiin"
    print "  check_permuation('foo', 'ofo') = ", \
        check_permutation('foo', 'ofo')

    print "  check_permuation('foos', 'ofo') = ", \
        check_permutation('foos', 'ofo')

    print "1.4 Palindrome Permutation"
    print "  palindrome_permuation('foo') = ", \
        palindrome_permutation('foo')
    print "  palindrome_permuation('fooo') = ", \
        palindrome_permutation('fooo')

    print "1.5 One Away"
    print "  one_away('pale', 'ple') = ", \
        one_away('pale', 'ple')
    print "  one_away('pales', 'pale') = ", \
        one_away('pales', 'pale')
    print "  one_away('pale', 'bale') = ", \
        one_away('pale', 'bale')
    print "  one_away('pale', 'bake') = ", \
        one_away('pale', 'bake')

    print "1.6 string compression"
    print "  string_compr('aabbb') = ", string_compr('aabbb')

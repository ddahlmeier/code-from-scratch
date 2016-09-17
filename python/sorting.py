"""Basic sorting algorithms in python."""
# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>

import random


def quick_sort(items):
    """sort list of items in natural order and return ordered list"""
    if items == []:
        # base case: empty list is ordered
        return []
    else:
        # recursion: concat sorted list smaller elements, pivot and
        # sorted list of larger elements
        pivot = items[0]
        return quick_sort(filter(lambda x: x <= pivot, items[1:])) + [pivot] +\
            quick_sort(filter(lambda x: x > pivot, items[1:]))


def merge_sort(items):
    """sort list of items in natural order and return ordered list"""
    def merge(left, right):
        merged = []
        i, j = 0, 0
        while i < len(left) and j < len(right):
            if left[i] <= right[j]:
                merged.append(left[i])
                i += 1
            else:
                merged.append(right[j])
                j += 1
        # add the remaining items after one list has been exhausted
        merged += left[i:]
        merged += right[j:]
        return merged

    if len(items) < 2:
        # base case: list of lenght one is ordered
        return items
    else:
        # split list into equal sizes sub lists
        half = len(items)/2
        left = items[:half]
        right = items[half:]
        # recursion: merge two sorted sub lists
        return merge(merge_sort(left), merge_sort(right))

if __name__ == "__main__":
    items = range(10)
    random.shuffle(items)
    print "Input", items
    print("quick sort: %s" % str(quick_sort(items)))
    print("merge sort: %s" % str(merge_sort(items)))

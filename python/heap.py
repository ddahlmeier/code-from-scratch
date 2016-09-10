"""Basic binary max heap in python.
https://en.wikipedia.org/wiki/Heap_(data_structure)
"""
# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>

import nose


def parent(i):
    """return index of parent"""
    return i//2


def left(i):
    """return index of left child"""
    return 2*i+1


def right(i):
    """return index of right child"""
    return 2*i+2


def swap(array, i, j):
    """swap elements at positions i and j"""
    array[i], array[j] = array[j], array[i]


def build_heap(array):
    """create a heap out of given array of elements."""
    for i in xrange(len(array)//2, -1, -1):
        heapify(array, i)


def heapify(heap, i, end=None):
    """restore heap property at position i assuming that children of i are
    valid heaps if end index is given ignore elements after end
    """
    if end is None:
        end = len(heap)-1
    largest, j = max([(heap[child(i)], child(i)) for child in [left, right]
                      if child(i) <= end] or [(heap[i], i)])
    if i != j and largest > heap[i]:
        swap(heap, i, j)
        heapify(heap, j, end)


def peek(heap):
    """ return max item without removing it"""
    return heap[0]


def pop(heap):
    """ return max item and remove it"""
    item = heap[0]
    # take the last item and put iit in front, then restore heap property
    heap[0] = heap[-1]
    heap = heap[:-1]
    heapify(heap, 0)
    return item


def insert(heap, item):
    """ insert item and restore heap property"""
    heap.append(item)
    sift_up(heap, len(heap)-1)


def sift_up(heap, i):
    """shift a value up the heap until heap proporty is restored"""
    if i > 0 and heap[parent(i)] < heap[i]:
        swap(heap, parent(i), i)
        sift_up(heap, parent(i))


def heap_sort(array):
    """sort array using heap"""
    build_heap(array)
    end = len(array)-1
    while end > 0:
        swap(array, 0, end)
        end -= 1
        heapify(array, 0, end)


def print_heap(heap, i=0, space=""):
    """ print heap in hierachical order"""
    print "%s%s" % (space, heap[i])
    if left(i) < len(heap):
        print_heap(heap, left(i), space + "  ")
    if right(i) < len(heap):
        print_heap(heap, right(i), space + "  ")


def test_build_heap():
    array = [2, 12, 17, 4, 5, 2, 4, 1]
    build_heap(array)
    # test heap property for each node
    for i in xrange(len(array)//2):
        if left(i) < len(array):
            nose.tools.assert_true(array[i] >= array[left(i)])
        if right(i) < len(array):
            nose.tools.assert_true(array[i] >= array[right(i)])


def test_heapify():
    array = [2, 4, 5]
    heapify(array, 0)
    nose.tools.assert_equals([5, 4, 2], array)


def test_heap_sort():
    array = [2, 12, 17, 4, 5, 2, 4, 1]
    heap_sort(array)
    nose.tools.assert_equals([1, 2, 2, 4, 4, 5, 12, 17], array)

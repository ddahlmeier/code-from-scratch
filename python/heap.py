"""Basic binary max heap in python.
https://en.wikipedia.org/wiki/Heap_(data_structure)
"""
# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


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
    print "heapify", heap, i, end
    print [(heap[child(i)], child(i)) for child in [left, right]
           if child(i) <= end]
    largest, j = max([(heap[child(i)], child(i)) for child in [left, right]
                      if child(i) <= end] or [(heap[i], i)])
    print "largest", largest, j
    if i != j and largest > heap[i]:
        print "swap", i, j
        swap(heap, i, j)
        heapify(heap, j)


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
    print "heap_sort", array
    build_heap(array)
    end = len(array)-1
    while end > 0:
        print "heap_sort", array
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

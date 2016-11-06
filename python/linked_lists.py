"""Linked lists examples from Cracking the coding interview Chapter 1"""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


class Node(object):

    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return "<node data= %s>" % str(self.data)

    def __repr__(self):
        return "<node data= %s>" % str(self.data)

    def append_to_tail(self, data):
        node = Node(data)
        n = self
        while(n.next):
            n = n.next
        n.next = node


def print_list(head):
    """print a linked list"""
    node = head
    while (node):
        print node
        node = node.next


def remove_dups(head):
    """remove duplicates from an unsorted list"""
    if head is None or head.next is None:
        return head
    seen = {head.data: 1}
    last = head
    node = head.next
    while (node):
        if node.data not in seen:
            # non duplicate, keep
            seen[node.data] = 1
            last = node
            node = node.next
        else:
            # delete duplicate
            node = node.next
            last.next = node
    return head


def k_last(head, k):
    """return k-th last element in list"""
    first = head
    second = head
    # first gets k nodes head start
    for i in xrange(k):
        first = first.next
        if first is None:
            print "list has less than k elements"
            return None
    # move pointers together
    while first:
        first = first.next
        second = second.next
    return second


def is_palindrome(head):
    """check if list is a palindrome"""
    fast = head
    slow = head
    stack = []
    while fast and fast.next:
        stack.append(slow.data)
        slow = slow.next
        fast = fast.next.next
    if fast:
        # odd lenght, slow is at the middle node
        slow = slow.next

    # compare reversed first half with second half of the list
    while slow:
        if stack.pop() != slow.data:
            return False
        slow = slow.next
    return True


def intersection(head1, head2):
    """check if two list intersect, return the intersecting node"""
    node1 = head1
    node2 = head2
    length1 = 0
    length2 = 0
    while node1.next:
        node1 = node1.next
        length1 += 1
    while node2.next:
        node2 = node2.next
        length2 += 1
    if node1 is not node2:
        # lists do not intersect
        print "no intersection"
        return None
    node1 = head1
    node2 = head2
    # chop off the uneven start lenght
    if length1 > length2:
        diff = length1 - length2
        for i in xrange(diff):
            node1 = node1.next
    elif length2 > length1:
        diff = length2 - length1
        for i in xrange(diff):
            node2 = node2.next
    # walk down both lists until we find the intersection
    while(node1 and node2):
        if node1 is node2:
            return node1
        node1 = node1.next
        node2 = node2.next

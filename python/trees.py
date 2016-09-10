"""Trees in python."""
# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>


import random


class Node(object):
    """base node class for trees"""

    def __init__(self, value):
        self.value = value
        self.children = []
        self.parent = None


class BinaryNode(Node):
    """binary tree with two cildren"""

    def __init__(self, value):
        super(BinaryNode, self).__init__(value)
        self.children = [None, None]
        self.left = self.children[0]
        self.right = self.children[1]

    def __repr__(self):
        return "<BinaryNode value = %s>" % self.value


def depth_first_search(node, value):
    """recursive depth first search. Return true if value is found,
    otherwise false
    """
    if node.value is value:
        return True
    if node.left and depth_first_search(node.left, value):
        return True
    if node.right and depth_first_search(node.right, value):
        return True
    return False


def binary_search(node, value):
    """recursive binary search. Return true if value is found,
    otherwise false
    """
    if node is None:
        return False
    print "at node", node.value
    if node.value is value:
        return True
    if value < node.value:
        return binary_search(node.left, value)
    else:
        return binary_search(node.right, value)


def random_tree():
    """generate random tree"""
    root = generate_node(None)
    return root


def generate_node(parent):
    """genrate node with ranodm value and recursive children"""
    node = BinaryNode(random.randint(1, 100))
    node.parent = parent
    if random.randint(0, 1):
        node.left = generate_node(node)
    if random.randint(0, 1):
        node.right = generate_node(node)
    return node


def print_tree(node, space=""):
    """ print tree in hierachical order"""
    print "%s%s" % (space, node.value)
    if node.left:
        print_tree(node.left, space + "  ")
    else:
        print "%s  -" % space
    if node.right:
        print_tree(node.right, space + "  ")
    else:
        print "%s  -" % space


if __name__ == "__main__":
    tree = BinaryNode(42)
    print tree.children

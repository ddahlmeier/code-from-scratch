"""Trees in python.
Basic data types and algorithms for binary search trees and red-black trees
https://en.wikipedia.org/wiki/Red%E2%80%93black_tree
"""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>

# Red black trees properties
# 1. A node is either red or black.
# 2. The root is black. This rule is sometimes omitted. Since the root
# can always be changed from red to black, but not necessarily vice
# versa, this rule has little effect on analysis.
# 3. All leaves (NIL) are black.
# 4. If a node is red, then both its children are black.
# 5. Every path from a given node to any of its descendant NIL nodes
# contains the same number of black nodes. Some definitions: the
# number of black nodes from the root to a node is the node's black
# depth; the uniform number of black nodes in all paths from root to
# the leaves is called the black-height of the red-black tree


import random


class Node(object):
    """base node class for trees"""

    def __init__(self, value, children=[]):
        self.value = value
        self.children = children
        self.parent = None

    def __str__(self, level=0):
        ret = "  "*level+repr(self.value)+"\n"
        for child in self.children:
            ret += child.__str__(level+1)
        return ret

    def __repr__(self):
        return "<BinaryNode value = %s>" % self.value


class BinaryNode(Node):
    """binary tree with two cildren"""

    def __init__(self, value):
        super(BinaryNode, self).__init__(value)
        self.children = [None, None]
        self.left = self.children[0]
        self.right = self.children[1]


class RedBlackNode(BinaryNode):
    """red-black tree node"""

    def __init__(self, value, color):
        super(RedBlackNode, self).__init__(value)
        self.children = [None, None]
        self.left = self.children[0]
        self.right = self.children[1]
        self.color = color

    def __repr__(self):
        return "<RedBlackNode value = %s color=%s>" % (self.value, self.color)


def grandparent(node):
    if node.parent and node.parent.parent:
        return node.parent.parent
    else:
        return None

def uncle(node):
    g = grandparent(node)
    if g is None:
        return None
    return g.right if n.parent == g.left else g.left


def insert(node, value):
    """insert a new value into red-black tree rooted at node"""
    if node.value > value:
        # insert left
        if node.left:
            insert(node.left, value)
        else:
            # add new node and color it red
            node.left = RedBlackNode(value, "red")
            node.left.parent = node
            # ensure that red-black properties are preserved
            rb_insert_case1(node.left)
    elif node.value < value:
        # insert right
        if node.right:
            insert(node.right, value)
        else:
            # add new node and color it red
            node.right = RedBlackNode(value, "red")
            node.right.parent = node
            # ensure that red-black properties are preserved
            rb_insert_case1(node.right)
    else:
        # value already exists, do nothing
        pass

    
def insert_case1(node):
    """current node is root of the tree. repaint it black to satify property 2"""
    if node.parent == None:
        node.color = "black"
    else:
        insert_case2(node)
        

def insert_case2(node):
    """current node's parent is black"""
    if node.parent.color == "black":
        # Tree is still valid
        return
    else:
        insert_case3(node)

    
def insert_case3(node):
    """both the parent and the uncle are red, repaint parent and uncle
    black and grandparent black"""
    u = uncle(node)
    if uncle and uncle.color == "red":
        node.parent.color = "black"
        u.color = "black"
        g = grandparent(node)
        g.color = "red"
        insert_case1(g)
    else:
        insert_case4(node)


def insert_case4(node):
    """parent is red but uncle is black, do a left (or right) rotation"""
    g = grandparent(node)
    if node == node.parent.right and node.parent == g.left:
        # rotate left
        saved_p = g.left
        saved_left = node.left
        g.left = node
        node.parent = g
        node.left = saved_p
        saved_p.parent = node
        saved_p.right = saved_left
        saved_left.parent = saved_p
        node = nodel.left
    elif node == node.parent.left and node.parent == g.right:
        # rotate right
        saved_p = g.right
        saved_right = node.right
        g.right = node
        node.parent = g
        node.right = saved_p
        saved_p.parent = node
        saved_p.left = saved_right
        saved_right.parent = saved_p
        node = nodel.right
    insert_case5(node)


def rotate_right(node):
    """right rotation"""
    saved_p = g.left
    saved_right = saved_p.right
    g.left = saved_p.right
    saved_p.right.parent = g
    saved_p.right = node
    saved_p.parent = node.parent
    node.parent = saved_p


def rotate_left(node):
    """left rotation"""
    saved_p = g.left
    saved_right = saved_p.right
    g.left = saved_p.right
    saved_p.right.parent = g
    saved_p.right = node
    saved_p.parent = node.parent
    node.parent = saved_p

    
def insert_case5(node):
    """parent is red but uncle is black, do a left (or right) rotation"""
    g = grandparetn(node)
    node.parent.color = "black"
    g.color = "red"
    if (node == node.parent.left):
        rotate_right(g)
    else:
        rotate_left(g)


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


class TrieNode(object):
    """ trie (prefix-tree) node implementation """

    def __init__(self, value):
        """ initialize trie node with some payload value"""
        self.value = value
        self.children = {}


def make_balanced_tree(height, n=2):
    """ create a balanced n-ary tree"""
    root = Node(0, [])
    queue = [(root, 0)]
    while queue:
        node, level = queue.pop(0)
        if level < height:
            for i in range(n):
                child = Node((n*node.value)+1+i, [])
                node.children.append(child)
                queue.append((child, level+1))
    return root


def make_trie(iterables):
    """ construct a trie from a set of iterables"""
    root = TrieNode(0)
    for iterable in iterables:
        node = root
        for item in iterable:
            if item not in node.children.iteritems():
                node.children[item] = TrieNode(0)
            node = node.children[item]
    return root


def print_trie(trie):
    """ construct a trie from a set of iterables"""
    stack = [('ROOT', trie, '')]
    while stack:
        key, node, indent = stack.pop()
        print "%s [%s] value: %s" % (indent, key, node.value)
        for key, child in node.children.iteritems():
            stack.append((key, child, indent + "  "))


if __name__ == "__main__":
    print("binary tree of height 3")
    tree = make_balanced_tree(3, 2)
    print(tree)

    print("3-ary tree of height 3")
    tree = make_balanced_tree(3, 3)
    print(tree)

    print('trie storing the words "awesome", "mix", "tape", "max", "table"')
    trie = make_trie(["awesome", "mix", "tape", "max", "table"])
    print_trie(trie)

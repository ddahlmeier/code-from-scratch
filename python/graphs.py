"""Graphs in python."""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>

from abc import ABCMeta, abstractmethod
import numpy as np
import random


class Graph(object):
    """Abstract base class for graphs"""
    __metaclass__ = ABCMeta

    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def get_edge(self, frm, to):
        pass

    @abstractmethod
    def adjacent(self, frm):
        pass

    @abstractmethod
    def set_edge(self, frm, to):
        pass


class GraphMatrix(Graph):
    """ Graph stored as a two dimensional adjacency matrix, nodes are
    stored as integer ids"""

    def __init__(self, n_nodes=10):
        self.adjacency = np.inf * np.ones((n_nodes, n_nodes))

    def get_edge(self, frm, to):
        return self.adjacency[frm, to]

    def adjacent(self, frm):
        return [to for to in self.adjacency[frm] if to != np.inf]

    def set_edge(self, frm, to, weight):
        self.adjacency[frm, to] = weight


class GraphDict(Graph):
    """ Graph stored as a adjacency list with dicts"""

    def __init__(self):
        self.adjacency = {}

    def get_edge(self, frm, to):
        g = self.adjacency.get(frm)
        if g:
            return g.get(to, np.inf)
        else:
            return np.inf

    def adjacent(self, frm):
        return self.adjacency[frm].keys()

    def set_edge(self, frm, to, weight):
        if frm not in self.adjacency:
            self.adjacency[frm] = {}
        self.adjacency[frm][to] = weight


def depth_first_search(graph, start, end):
    """traverse graph in depth first search from start to end
    return true if value is found otherwise false
    """
    stack = [start]
    while stack:
        node = stack.pop()
        if node is end:
            return True
        for to in graph.adjacent(node):
            stack.append(to)
    return False


def random_graph(Graph, n_nodes, n_edges):
    if Graph is GraphMatrix:
        g = GraphMatrix(n_nodes)
    elif Graph is GraphDict:
        g = GraphDict()
    else:
        raise Exception("Unknown graph type %s" % Graph)
    for _ in xrange(n_edges):
        g.set_edge(random.randint(0, n_nodes-1), random.randint(0, n_nodes-1),
                   random.randint(1, 10))
    return g

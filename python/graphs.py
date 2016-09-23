"""Graphs in python."""

# Author: Daniel Dahlmeier <ddahlmeier@gmail.com>

from abc import ABCMeta, abstractmethod
import numpy as np
import random
from itertools import chain
from operator import itemgetter
import heapq


def unique(iter):
    """Helper class to return list of unique items in iter"""
    return list(set(iter))


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

    @abstractmethod
    def nodes(self):
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

    def nodes(self):
        return range(self.adjacency.shape[0])


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
        node = self.adjacency.get(frm, None)
        return node.keys() if node else []

    def set_edge(self, frm, to, weight):
        if frm not in self.adjacency:
            self.adjacency[frm] = {}
        self.adjacency[frm][to] = weight

    def nodes(self):
        return unique(chain(self.adjacency.keys(),
                            *(d.keys() for d in self.adjacency.values())))


def depth_first_search(graph, start, end):
    """traverse graph in depth first search from start to end
    return true if value is found otherwise false
    """
    stack = [start]
    visited = {n: False for n in graph.nodes()}
    print "depth first search", start, "->", end
    while stack:
        node = stack.pop()
        print "visit", node
        visited[node] = True
        if node is end:
            return True
        for to in (neighbour for neighbour in graph.adjacent(node)
                   if not visited[neighbour]):
            stack.append(to)
    return False


def breath_first_search(graph, start, end):
    """traverse graph in breath first search from start to end
    return true if value is found otherwise false
    """
    queue = [start]
    visited = {n: False for n in graph.nodes()}
    print "breath first search", start, "->", end
    while queue:
        node = queue.pop(0)
        print "visit", node
        visited[node] = True
        if node is end:
            return True
        for to in (neighbour for neighbour in graph.adjacent(node)
                   if not visited[neighbour]):
            queue.append(to)
    return False


def trace_back(graph, backpointers, node):
    """ return path from node through backpointers"""
    path = []
    while node:
        path.append(node)
        node = backpointers.get(node)
    return list(reversed(path))


def dijkstra(graph, start, end):
    """Dijkstra shortest-path search"""
    queue = [(0, start)]  # priority queue for nodes
    distance = {n: np.inf for n in graph.nodes()}  # shortest distance to nodes
    distance[start] = 0
    visited = {n: False for n in graph.nodes()}
    backpointers = {}  # store back pointers for tracing back path
    print "dijkstra search", start, "->", end
    while queue:
        dist, node = queue.pop(0)
        # ignore visited nodes, can double visit due to queue duplicates
        if visited[node]:
            continue
        print "visit", node, " with distance", dist
        visited[node] = True
        if node is end:
            return (dist, trace_back(graph, backpointers, node))
        for to in (neighbour for neighbour in graph.adjacent(node)
                   if not visited[neighbour]):
            print "check", node, " ->", to
            # update distance if we have found a new shortest path
            if distance[node] + graph.get_edge(node, to) < distance[to]:
                print "update shortest path"
                distance[to] = distance[node] + graph.get_edge(node, to)
                backpointers[to] = node
            # add neighbour to queue
            heapq.heappush(queue, (distance[to], to))
    return (np.inf, [])


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

# This helps to generate an initial S-Box.
from random import randint


def gen():
    """Generates a list containing no.s below 256 only."""
    s = []
    while len(s) != 256:
        num = randint(0, 256)
        if num not in s:
            s.append(num)
    return s


def undirected(array):
    """Creates an undirected graph for all the 256 nodes(elements) of the list.

    Undirected graph will be a dictionary with key as node and value is a list,
    such that `i`th node will have list containing cost of edges to vertices
    starting from `i+1`.
    """
    graph = {}
    for vertex in range(len(array)):
        graph[vertex] = []
        for x in range(256 - vertex - 1):
            graph[vertex].append(randint(0, 256))
    return graph

print(undirected(gen()))

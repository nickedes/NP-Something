# This helps to generate an initial S-Box.
from random import randint
import json


def gen():
    """Generates a list containing no.s below 256 only."""
    s = []
    while len(s) != 256:
        num = randint(0, 256)
        if num not in s:
            s.append(num)
    with open('data.txt', 'w') as f:
        f.write(json.dumps(s))
    return s


def undirected(array, num=0):
    """Creates an undirected graph for nodes(elements) of the list.

    Undirected graph will be a dictionary with key as node and value is a list,
    such that `i`th node will have list containing cost of edges to vertices
    starting from `i+1`.

    Parameters
    ----------
    array : list
        List contains unique 256 no.s in the range 0-256.
    num : int
        The nodes for the graph start from 8**num till 8**(num+1).
    """
    graph = {}
    for vertex in range(len(array[8*num:8*(num+1)-1])):
        graph[vertex % 8] = []
        for x in range(8 - (vertex % 8) - 1):
            graph[vertex % 8].append(randint(0, 256))
    return graph

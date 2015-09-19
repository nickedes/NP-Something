# This helps to generate an initial S-Box.
from random import randint
from test import nonlinearity


def gen():
    """Generates a list containing no.s below 256 only."""

    # Gen with PWLCM
    # non = {}
    # s = []
    # for i in range(1, 10):
    #     for j in range(1, 10):
    #         s = []
    #         if j == 5 or i == j or (j == 4 and i == 1):
    #             continue
    #         x, p = i/10, j/10
    #         for k in range(1000):
    #             x = pwlcm(x, p)

    #         while len(s) != 256:
    #             x = pwlcm(x, p)
    #             val = int(x*10**5) % 256
    #             if val not in s:
    #                 s.append(val)
    #         # print (i)
    #         # print (j)
    #         non[sum(nonlinearity(s))/8] = [i, j]
    #         # print(sum(nonlinearity(s))/8)
    # print(non)
    # return s

    s = []
    x, p = 0.1, 0.9
    for k in range(1000):
        x = pwlcm(x, p)

    while len(s) != 256:
        x = pwlcm(x, p)
        val = int(x*10**5) % 256
        if val not in s:
            s.append(val)

    return s


def pwlcm(x, p):
    """

    """
    if 0 < x <= p:
        return x/p
    elif p < x < 1:
        return (1-x)/(1-p)
    else:
        print(x)
        raise ValueError


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
            graph[vertex % 8].append(randint(1, 255))
    return graph

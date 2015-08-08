def travelling():
    """
    """
    pass


def dist(i, j):
    """
    Returns the weight of edge from i -> j or vice-versa.
    The graph is undirected.

    Paramters
    ---------
    i : int
    j : int
    """
    if i < j:
        return graph[i][j-1]
    elif j < i:
        returb graph[j][i-1]
    else:
        return 0


def cost(set_Vertices, node):
    """
    cost of the minimum cost path visiting each vertex in set S exactly once,
    starting at 0 and ending at node.

    Paramters
    ---------
    set_Vertices : set
        A set of vertices of graph.

    node : int
        The vertex to which we need minimum cost.
    """
    if len(set_Vertices) == 2:
        pass
    else:
        pass
    pass

"""
>>> s = set()
>>> s |= set(list(range(24)))
>>> s
{0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23}
>>> 
"""

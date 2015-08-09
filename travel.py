from initial import gen, undirected


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
    try:
        if i < j:
            return graph[i][j-i-1]
        elif j < i:
            return graph[j][i-j-1]
        else:
            return 0
    except:
        print(i, j)
        return 0


def cost(set_Vertices, node):
    """
    Returns cost of the minimum cost path visiting each vertex in set
    set_Vertices exactly once, starting at 0 and ending at node.

    Paramters
    ---------
    set_Vertices : set
        A set of vertices of graph.

    node : int
        The vertex to which we need minimum cost.
    """
    if len(set_Vertices) == 2:
        return dist(0, list(set_Vertices)[1])
    else:
        temp = []
        for j in set_Vertices:
            if j != node and j != 0:
                temp.append(cost(set_Vertices-{node}, j) + dist(j, node))
        return min(temp)
    pass


if __name__ == '__main__':
    array = gen()
    graph = undirected(array)
    # print(graph[0])
    # print(graph[253][254-1-253])
    # print(dist(253,254))
    set_Vertices = set()
    set_Vertices |= set(list(range(256)))
    print(cost(set_Vertices, 0))

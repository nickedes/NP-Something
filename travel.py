from initial import gen, undirected
from itertools import permutations as per


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
        i, j = i % 8, j % 8
        if i < j:
            return graph[i][j-i-1]
        elif j < i:
            return graph[j][i-j-1]
        else:
            return 0
    except:
        print(i, j)
        return 0


def cost(set_Vertices):
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
    cost_path = 0
    for node in range(len(set_Vertices)-1):
        cost_path += dist(set_Vertices[node], set_Vertices[node+1])
    return cost_path


if __name__ == '__main__':
    array = gen()
    graph = undirected(array, 0)
    all_perms = list(per(range(8)))
    cost_path = []
    paths = {}
    for perm in all_perms:
        tupl = perm + (perm[0], )
        if cost(tupl) not in cost_path:
            cost_path.append(cost(tupl))
        if cost(tupl) not in paths:
            paths[cost(tupl)] = tupl
    # print(paths, cost_path)
    print(min(cost_path), paths[min(cost_path)])
    # graph

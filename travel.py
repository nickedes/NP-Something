from initial import gen, undirected
from itertools import permutations as per
import json


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
        print(graph)
        exit()
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
    all_perms = list(per(range(8)))
    array_mod = []
    for num in range(32):
        print(num)
        graph = undirected(array, num)
        cost_path = []
        paths = {}
        for perm in all_perms:
            tupl = perm + (perm[0], )
            path_val = cost(tupl)
            if path_val not in cost_path:
                cost_path.append(path_val)
            if path_val not in paths:
                paths[path_val] = tupl
        # print(paths, cost_path)
        print(min(cost_path), paths[min(cost_path)])
        for index in paths[min(cost_path)]:
            if array[8*num + index] not in array_mod:
                array_mod.append(array[8*num + index])
    with open('data2.txt', 'w') as f:
        f.write(json.dumps(array_mod))
    # graph

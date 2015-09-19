from initial import gen, undirected
from bijective import is_bijective
from itertools import permutations as per
from test import value_nonl
from datetime import datetime
from json import dumps
from data import limit


def getfilename():
    """
    Returns the current timestamp and will be used as filename.
    """
    timestamp = str(datetime.now())[:-7]
    return timestamp.replace(' ', '-')


def travelling(array, num):
    """
    """
    global graph
    graph = undirected(array, num)
    cost_path = []
    paths = {}
    for perm in all_perms:
        tupl = perm + (perm[0], )
        path_val = cost(graph, tupl)
        if path_val not in cost_path:
            cost_path.append(path_val)
        if path_val not in paths:
            paths[path_val] = tupl
    return cost_path, paths


def dist(graph, i, j):
    """
    Returns the weight of edge from i -> j or vice-versa.
    The graph is undirected.

    Paramters
    ---------
    i : int
    j : int
    graph : Dict
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
        exit()


def substitution(array, array_mod, num):
    """
    """

    cost_path, paths = travelling(array, num)
    for index in paths[min(cost_path)]:
        if array[8*num + index] not in array_mod:
            array_mod.append(array[8*num + index])
    return array_mod


def cost(graph, set_Vertices):
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
        cost_path += dist(graph, set_Vertices[node], set_Vertices[node+1])
    return cost_path


if __name__ == '__main__':
    graphs = []
    initial_non = value_nonl(gen())
    non_sbox = {initial_non: gen()}
    for var in range(64):
        print(var)
        array = gen()
        if is_bijective(array):
            all_perms = list(per(range(8)))
            array_mod = []
            for num in range(32):
                array_mod = substitution(array, array_mod, num)
                graphs.append(graph)
            nn_array_mod = value_nonl(array_mod)
            if nn_array_mod > limit:
                non_sbox[nn_array_mod] = [array_mod, graphs]
                print(value_nonl(array), nn_array_mod)
        else:
            print('Is not bijective!')
    if max(non_sbox) > limit:
        with open('data/part-1/'+getfilename(), 'a') as f:
            f.write(dumps(non_sbox))
    print(non_sbox.keys(), max(non_sbox.keys()))

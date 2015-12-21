# Der's more to travelling baby!
from data import sbox, limit
from random import randint
from travel import (
    substitution,
    getfilename,
    value_nonl,
    per,
    is_bijective,
    dumps,
    cost
)
from time import time


def more_travel(array):
    """
    """
    if is_bijective(array):
        all_perms = list(per(range(8)))
        for var in range(64):
            array_mod = []
            for num in range(32):
                array_mod, graph = substitution(
                    all_perms, array, array_mod, num)
                graphs.append(graph)
            nn_array_mod = value_nonl(array_mod)
            print(var, nn_array_mod)
            if nn_array_mod > limit:
                non_sbox[nn_array_mod] = [array_mod, graphs]
                print(value_nonl(array), nn_array_mod)
    else:
        print('Is not bijective!')
    return 1


def graphy():
    """
    Gives an undirected graph for the 8 vertices.
    """
    graph = {}
    for vertex in range(8):
        graph[vertex] = []
        for x in range(8 - vertex - 1):
            temp = randint(1, 255)
            graph[vertex].append(temp)
    return graph


def travelling(all_perms):
    """
    """
    graph = graphy()
    cost_path = []
    paths = {}
    for perm in all_perms:
        tupl = perm + (perm[0], )
        path_val = cost(graph, tupl)
        if path_val not in cost_path:
            cost_path.append(path_val)
        if path_val not in paths:
            paths[path_val] = tupl
    return cost_path, paths, graph


def selected_travel(nodes):
    """
    """
    # PHEW! Bug fix!!!!!
    array = list(sbox)
    indices = {}
    # get indices of all the above nodes
    for node in nodes:
        indices[array.index(node)] = node
    maps, num = {}, 0
    for node in indices:
        maps[num] = node
        num += 1
    all_perms = list(per(range(8)))
    cost_path, paths, graph = travelling(all_perms)
    min_path = paths[min(cost_path)]
    new_mapping = {}
    for num in range(len(min_path) - 1):
        new_mapping[maps[num]] = indices[maps[min_path[num]]]
    # Substitute! the sequence
    for node in new_mapping:
        array[node] = new_mapping[node]
    return array, graph

if __name__ == '__main__':
    # We start Preti!
    start = time()
    graphs = []
    non_sbox = {value_nonl(sbox): sbox}
    # select 8 max nodes
    nodes = list(range(255, 247, -1))
    # select 8 mid nodes
    # nodes = list(range(165, 157, -1))
    print("observed", "expected")
    for var in range(50):
        sbox_mod, graph = [], {}
        sbox_mod, graph = selected_travel(nodes)
        # print(value_nonl(sbox_mod), max(non_sbox), round(time()-start))
        print(value_nonl(sbox_mod), "  ", max(non_sbox))
        if value_nonl(sbox_mod) > limit:
            non_sbox[value_nonl(sbox_mod)] = [sbox_mod, graph]
        print()
    if max(non_sbox) > limit:
        with open('data/part-2/'+getfilename(), 'a') as f:
            f.write(dumps(non_sbox))
    print(non_sbox.keys(), max(non_sbox.keys()))

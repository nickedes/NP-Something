# Der's more to travelling baby!
from data import sbox
from travel import (
    substitution,
    getfilename,
    limit,
    value_nonl,
    per,
    is_bijective,
    dumps
)


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
    pass


def selected_travel(array):
    """
    """
    # select 8 max nodes
    nodes = list(range(255, 247, -1))
    # get indices of all the above nodes
    indices = {}
    for node in nodes:
        indices[node] = array.index(node)

    maps, num = {}, 0
    for node in indices:
        maps[num] = node
        num += 1
    return maps

if __name__ == '__main__':
    graphs = []
    non_sbox = {value_nonl(sbox): sbox}
    # more_travel(sbox)
    # if max(non_sbox) > limit:
    #     with open('data/part-2/'+getfilename(), 'a') as f:
    #         f.write(dumps(non_sbox))
    print(selected_travel(sbox))
    print(non_sbox.keys(), max(non_sbox.keys()))

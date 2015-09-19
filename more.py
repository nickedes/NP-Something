# Der's more to travelling baby!
from data import sbox
from bijective import is_bijective
from itertools import permutations as per
from test import value_nonl
from data import limit
from travel import substitution


def more_travel(array):
    """
    """
    non_sbox = {}
    if is_bijective(array):
        all_perms = list(per(range(8)))
        array_mod = []
        for num in range(32):
            array_mod, graph = substitution(all_perms, array, array_mod, num)
            graphs.append(graph)
        nn_array_mod = value_nonl(array_mod)
        # if nn_array_mod > limit:
        non_sbox[nn_array_mod] = [array_mod, graphs]
        print(value_nonl(array), nn_array_mod)
    else:
        print('Is not bijective!')
    return non_sbox

# if max(non_sbox) > limit:
#         with open('data/part-1/'+getfilename(), 'a') as f:
#             f.write(dumps(non_sbox))
#     print(non_sbox.keys(), max(non_sbox.keys()))
graphs = []
print(more_travel(sbox))

# This helps to generate an initial S-Box.
from random import randint


def gen():
    """Generates an array."""
    s = []
    while len(s) != 256:
        num = randint(0, 256)
        if num not in s:
            s.append(num)
    print(s)

gen()

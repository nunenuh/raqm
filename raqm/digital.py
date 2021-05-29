import math

def root(n, base=9):
    return n % base or n and base

def root_with_factor(n, base=9):
    base_factor = math.floor((n/base))
    root = n % base or n and base
    if get_factor:
        return root, base_factor
    return root



    
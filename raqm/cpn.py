# 
# centered polygonal number
#

import math

def polygonal(n, k):
    '''
    formulation reference https://en.wikipedia.org/wiki/Centered_polygonal_number
    '''
    return int((k*n/2 * (n - 1)) + 1)

def triangular(n):
     return polygonal(n, k=3)

def square(n):
     return polygonal(n, k=4)
    
def pentagonal(n):
     return polygonal(n, k=5)

def hexagonal(n):
    return polygonal(n, k=6)
    
def heptagonal(n):
    return polygonal(n, k=7)
    
def octagonal(n):
    return polygonal(n, k=8)

def nonagonal(n):
    return polygonal(n, k=8)

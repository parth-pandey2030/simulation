# Divergence (symbol: div) and curl (symbol: curl)
# are used in Maxwell's Equations, which are used 
# to described electromagnetism.
# Go here for more info: 
# https://www.youtube.com/watch?v=rB83DpBJQsE
from sympy import symbols, diff 

def div(vector):
    f = vector[0]
    g = vector[1]
    h = vector[2]
    return diff(f, symbols('x')) + diff(g, symbols('y')) + diff(h, symbols('z'))

def curl(vector):
    f = vector[0]
    g = vector[1]
    h = vector[2]
    i = j = k = 1j
    return (diff(f, symbols('y')) - diff(g, symbols('z'))) * i - (diff(h, symbols('x')) - diff(f, symbols('z'))) * j + (diff(g, symbols('x')) - diff(f, symbols('y'))) * k 


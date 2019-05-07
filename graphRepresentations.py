# This first representation of a graph is an adjacency list
# we use a list of sets to represent it in python 
a, b, c, d, e, f, g, h = range(8)
N = [
        {b, c, d, e, f},
        {c, e},
        {d},
        {e},
        {f},
        {c, g, h},
        {f, h},
        {f, g}
    ]

# We could also use a list of list to avoid the slightly larger overhead of the sets 

N_prime = [
        [b, c, d, e, f],
        [c, e],
        [d],
        [e],
        [f],
        [c, g, h],
        [f, h],
        [f, g]
    ]

# A different variation using dictionaries instead of sets. Now we can represent a weighted graph. 

G = [
        {b:2, c:1, d:3, e:9, f:4},
        {c:4, e:3},
        {d:8},
        {e:7},
        {f:5},
        {c:2, g:2, h:2},
        {f:1, h:6},
        {f:9, g:8}
    ]
# If we want to use an adjacency matrix, we can represented as a list of lists in python
inf = float('inf')
#     a, b, c, d, e, f, g, h
W = [[0, 2, 1, 3, 9, 4, inf, inf], # a 
    [inf, 0, 4, inf, 3, inf, inf, inf], # b 
    [inf, inf, 0, 8, inf, inf, inf, inf], # c 
    [inf, inf, inf, 0, 7, inf, inf, inf], # d 
    [inf, inf, inf, inf, 0, 5, inf, inf], # e 
    [inf, inf, 2, inf, inf, 0, 2, 2], # f 
    [inf, inf, inf, inf, inf, 1, 0, 6], # g 
    [inf, inf, inf, inf, inf, 9, 8, 0]] # h

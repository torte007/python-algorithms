# This answer had a quadratic time complexity. 
from random import randrange
seq = [randrange(10**10) for i in range(100)]
dd = float("inf")
for x in seq:
    for y in seq:
        if x == y:
            continue
        d = abs(x-y)
        if d < dd:
            xx, yy, dd = x, y, d
# If we want a better answer, we can sort the sequence first and just
# go through the sequence
seq.sort()
dd = float("inf")
for i in range(len(seq)-1):
    x, y = seq[i], seq[i+1]
    if x == y:
        continue
    d = abs(x-y)
    if d < dd:
        xx, yy, dd = x, y, d

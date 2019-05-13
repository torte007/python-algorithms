def trav(seq, i=0):
    if i == len(seq):
        return 
    trav(seq, i+1)
print("Using trav with 100 works fine")
trav(range(100))

try:
    print("Using trav with 1000 gives you a RuntimeError because we've exceeded the maximum recursion depth")
    trav(range(1000))
except RecursionError:
    print("RecursionError")

print("Sometimes the iterative solution is better")

def iterative_trav(seq):
    for i in seq:
        pass
    return

# %% 
# We need to be careful of maximum recursion depth exceeded 
def fib1(n: int) -> int:
    return fib1(n - 1) + fib1(n - 2)

# if __name__ == '__main__':
#     print(fib1(5))

# %%
def fib2(n: int) -> int: 
    if n < 2: 
        return n
    return fib2(n - 2) + fib2(n - 1)

# if __name__ == "__main__":
#     print(fib2(5))

# %%
# Using Memoization

# Memoization is a technique in which you store the results
# of computational tasks when they are completed so that 
# when you need them again, you can look them up instead of
# needing to compute them a second or millionth time. 

# %%
# Memoization without a decorator
from typing import Dict

memo: Dict[int, int] = {0: 0, 1: 1}

# I believe that we could also do memo2 = {0: 0, 1: 1} and it would be
# essentialy the same thing

def fib3(n: int) -> int: 
    if n not in memo: 
        memo[n] = fib3(n - 1) + fib3(n - 2)
    return memo[n]

# if __name__ == "__main__":
#     print(fib3(5)) 
#     print(fib3(50))

# %%
# Using memoization with a decorator 
# In the book they call it automatic memoization

from functools import lru_cache

@lru_cache(maxsize=None)
def fib4(n: int) -> int:
    if n < 2: 
        return n
    return fib4(n - 1) + fib4(n - 2)

# if __name__ == "__main__":
#     print(fib4(50))

#%%
# Iterative Approach

# This is actually the most efficient method for finding fibonacci
def fib5(n: int) -> int: 
    if n == 0: 
        return n
    last: int = 0
    next: int = 1
    for _ in range(1, n):
        last, next = next, last + next
    return next

# if __name__ == "__main__":
#     print(fib4(50))


#%%
# Generating fibonacci numbers with a generator
# What is a generator? 
#   They are a simple way of creating iterators. 

# When the generator is iterated, each iteration will spew a 
# value from the Fibonacci sequence using a yield statement.

from typing import Generator

def fib6(n: int) -> Generator[int, None, None]: 
    yield 0 # Special case
    if n > 0: 
        yield 1
    last: int = 0 
    next: int = 1     
    for _ in range(1, n):
        last, next = next, last + next
        yield next # main generation step

if __name__ == "__main__":
    # Now we can use this function like range()
    for i in fib6(50):
        print(i)
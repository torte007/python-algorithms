# The rules of the towers of hanoi are: 
# 
# - Only one disc can be moved at a time. 
# - The topmost disc of any tower is the only one available for moving. 
# - A wider disc can never be atop a narrower disc. 


from typing import TypeVar, List, Generic

T = TypeVar("T")

class Stack(Generic[T]):
    def __init__(self) -> None:
        self._container: List[T] = []
    
    def push(self, item: T) -> None:
        self._container.append(item)

    def pop(self) -> T:
        return self._container.pop()

    def __repr__(self) -> str:
        return repr(self._container)

def hanoi(begin: Stack[int], end: Stack[int], temp: Stack[int], n: int) -> None:
    if n == 1:
        end.push(begin.pop()) # Move a single disc
    else:
        hanoi(begin, temp, end, n - 1) # Move the upper n-1 discs from tower A to B (the temporary tower), using C as the in-between.
        hanoi(begin, end, temp, 1) # Move the single lowest disc from A to C
        hanoi(temp, end, begin, n - 1) # Move the n - 1 discs from tower B to C, using A as the in-between

if __name__ == "__main__":
    num_discs: int = 3
    tower_a: Stack[int] = Stack()
    tower_b: Stack[int] = Stack()
    tower_c: Stack[int] = Stack()
    for i in range(1, num_discs + 1):
        tower_a.push(i)
    hanoi(tower_a, tower_c, tower_b, num_discs)
    print(tower_a)
    print(tower_b)
    print(tower_c)


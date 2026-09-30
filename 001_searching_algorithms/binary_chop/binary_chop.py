import random
# binary search algorithm/binary chop
# one of the most efficient divide-and-conquer search algorithms 
"""
    Note: Never use a list of 1 billion elements in a test, it will take forever to run. In 
    CPython, this would consume tens of gigabytes of memory and likely cause a MemoryError.
    Take a look at it:
        A = list(range(1, 1_000_000, 2))
        A.extend(list(range(1_000_000, int(10e6), 2)))
        A.extend(list(range(int(10e6), int(1e9), 2))) 

    Advantages of using range instead of list:
    1. Memory Efficiency: 
        The range object generates numbers on-the-fly(generated on-demand) and 
        does not store them in memory, making it more memory-efficient than a list.
    2. Performance: 
        The range object is implemented in C and optimized for performance, 
        making it faster than a list for generating sequences of numbers.
    3. Readability:
        The range object is more concise and easier to read than a list, 
        especially for large ranges of numbers.
    4. criação instantânea;
    5. indexação O(1);
    6. A[-1] funciona normalmente.
"""
A = range(1_000_000, int(1e9), 2)

def binary_chop(T):
    # gets the element index
    left = 0
    right = len(A) - 1

    while left <= right:
        middle = (left + right) // 2
        if A[middle] < T:
            left = middle + 1
            continue
        elif A[middle] > T:
            right = middle -1
            continue
        elif A[middle] == T:
            return middle
    return -1

print("binary search: ")
print(binary_chop(1_000_000))
print(binary_chop(1_000_002))
print(binary_chop(3_600_000))
print(binary_chop(3_600_001))
print(binary_chop(7_486_366))


def slow_chop(T):
    # gets the element index
    for i in range(len(A)):
        if A[i] == T:
            return i
    return -1

print("\nslow search: ")
print(slow_chop(3_600_000))
print(slow_chop(3_600_001)) # this one will take a long time to run, as it will iterate through the entire list to find the element.


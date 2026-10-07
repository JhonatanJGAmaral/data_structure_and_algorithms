"""
INTERESTING THERMS:
    > devide-and-conquer algorithm
    > heapsort algorithm
    > in-place, non-in-place/out-of-place algorithms
"""

# https://en.wikipedia.org/wiki/Quicksort
"""
Quicksort is an effiecient, general-purpose sorting algorithm. Quicksort was developed by 
British computer scientist Tony Hoare in 1959 and published in 1961. It is still a commonly 
used algorithm for sorting. Overall, it is slightly faster than merge sort and heapshort for 
randomized data, particularly on larger distributions. 

Quicksort is a divide-and-conquer algorithm. It works by selecting a "pivot" element from the
array and partitioning the other elements into two sub-arrays, according to whether they are
less than or greater that the pivot. For this reason, it is sometimes called:
    "partition-exchange sort".
The subs-arrays are then sorted recursively. This can be done in-place (https://en.wikipedia.org/wiki/In-place_algorithm), 
requiring small additional ammounts of memory to perform sorting. 

[in-place]
----> in-place algorithm is meant to operate changes directly on the the input data strucure
----> withou requiring extra space proportional to the input size. In the other words, it 
----> modifies the input in place, without creating a separate copy of the data structure. 
----> An algorithm which is not in-place is sometimes called not-inplace or out-of-place.
----> [...]
[...]

[...], so that quicksort is really a family of closely related algorithms. 
"""

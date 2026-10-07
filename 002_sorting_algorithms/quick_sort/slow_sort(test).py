
def generate_random_list(size, lower_bound=0, upper_bound=100):
    """
    Generates a random list of integers.

    :param size: The size of the list to generate.
    :param lower_bound: The lower bound for the random integers (inclusive).
    :param upper_bound: The upper bound for the random integers (exclusive).
    :return: A list of random integers.
    """
    import random
    return [random.randint(lower_bound, upper_bound - 1) for _ in range(size)]

A = generate_random_list(100_000, 0, 100_000)
# print(A[:10])
# print(A[-10:])
"""
    B = [2, 3, 1, 5, 4, 6, 8, 7, 9, 0]
    B = [2, 1, 3, 5, 4, 6, 8, 7, 9, 0]
    B = [2, 1, 3, 5, 4, 6, 8, 7, 9, 0]
    B = [2, 1, 3, 4, 5, 6, 8, 7, 9, 0]
    B = [2, 1, 3, 4, 5, 6, 8, 7, 9, 0]
    B = [2, 1, 3, 4, 5, 6, 8, 7, 9, 0]
    B = [2, 1, 3, 4, 5, 6, 7, 8, 0, 9]
    B = [2, 1, 3, 4, 5, 6, 7, 0, 8, 9]
    B = [2, 1, 3, 4, 5, 6, 0, 7, 8, 9]
    B = [2, 1, 3, 4, 5, 0, 6, 7, 8, 9]
    [...]
"""

def slow_sort_1(A):
    while True:
        keep_loop = False
        dif_list = []
        occ = -1
        for i, val in enumerate(A):
            j = i + 1
            if j < len(A):
                occ += 1
                dif_list.append(A[j] - A[i]) 

                if A[i] > A[j]:
                    A[i], A[j] = A[j], A[i]
                    if occ >= 1 and dif_list[occ] < dif_list[occ - 1]:
                        keep_loop = True
            else:
                break
        if not keep_loop: break
    return A


def slow_sort_2(A):
    def trade_positions(A, i, j, keep_loop, occ, dif_list):
        j = i + 1
        if i>= 0 and j >= 1 and j < len(A):
            occ += 1
            dif_list.append(A[j] - A[i]) 

            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
                if occ >= 1 and dif_list[occ] < dif_list[occ - 1]:
                    A, i, j, keep_loop, occ, dif_list = trade_positions(
                        A, i-1, j, keep_loop, occ, dif_list
                    )
                    keep_loop = True
        elif keep_loop: 
            keep_loop = ~keep_loop
                    
        return A, i, j, keep_loop, occ, dif_list

    while True:
        keep_loop = False
        dif_list = []
        occ = -1
        j = 0
        for i, val in enumerate(A):
            A, i, j, keep_loop, occ, dif_list = trade_positions(
                A, i, j, keep_loop, occ, dif_list
            )
            if j >= len(A): break
        if not keep_loop: break
    return A


"""
def algo_test_4(list_to_sort):
    # working with a bidimensional (2 x n/2) matrix without creating it itself
    # mtx_dimen
    Y, X = (2, len(list_to_sort) // 2)

    for idx, val in enumerate(list_to_sort):
        curr_line = idx // Y
        curr_column = idx % Y
        pass
"""

def test_slow_sort_1():
    # finish quickly sort algorithm
    B = [2, 3, 1, 5, 4, 6, 8, 7, 9, 0]
    B_sorted = slow_sort_1(B)
    print(B_sorted)

    # but the same does not work with a big list; it takes too long to sort it
    # A = generate_random_list(100_000, 0, 100_000)
    A = generate_random_list(100, 0, 100_000)
    print(f'\nfirst 10 elements of A: {A[:10]}\nsize:{len(A)}')
    A_sorted = slow_sort_1(A)
    print(A_sorted)

# test_slow_sort_1()

def test_slow_sort_2():
    C = [2, 3, 1, 5, 4, 6, 8, 7, 9, 0]
    C_sorted = slow_sort_2(C)
    print(C_sorted)

    D = generate_random_list(5_000, 0, 100_000)
    D_sorted_1 = slow_sort_1(D.copy()) # This one ends up being faster than the second slow algorithm
    print(D_sorted_1[:10], D_sorted_1[-10:])
    
    D_sorted_2 = slow_sort_2(D.copy())
    print(D_sorted_2[:10], D_sorted_2[-10:])

# test_slow_sort_2()

import matplotlib.pyplot as plt
import numpy as np

def slow_sort_3(A):
    left = 0
    right = len(A) - 1
    mid = len(A) // 2
    left_stopped = False
    right_stopped = False
    full_sorted = False
    curr_average = 0
    num_elem = 0
    count_loop = 0
    # ---
    while not full_sorted:
        curr_val_list = []
        while not left_stopped:
            if left < len(A) and A[left] > A[mid]:
                left_stopped = True
            else:
                left += 1
            if left >= len(A):
                left = 0
                break
            num_elem += 1
            curr_val_list.append(A[left])
        
        while not right_stopped:
            if right >= 0 and A[right] < A[mid]:
                right_stopped = True
            else:
                right -= 1
            if right < 0:
                right = len(A)-1
                break
            num_elem += 1
            curr_val_list.append(A[right])
        
        if not left_stopped or not right_stopped:
        # if not left_stopped and not right_stopped:
            count_loop += 1
            print("aaaaa")
            if count_loop > 1:
                print("bbbb")
                xpoints = np.array([idx for idx in enumerate(A)])
                ypoints = np.array(A)

                plt.plot(xpoints, ypoints)
                plt.axis('off')
                # plt.xticks(list(range(0, 101, 10)))
                # plt.yticks([])
                plt.show()

                return
            continue

        curr_average += sum(curr_val_list)//num_elem

        A[left], A[right] = A[right], A[left]
        left_stopped = False
        right_stopped = False
        # print(A)

        if right < left:
            mid = mid+1 if A[mid] > curr_average else mid-1
        # print(mid)
        #     mid -= 1
        # elif left >= len(A)-1:
        #     mid += 1

        # if mid < len(A):
        #     A[left], A[right] = A[right], A[left]
        #     left_stopped = False
        #     right_stopped = False
        #     print(A)
        #     continue
        
        # full_sorted = True
    return A

def min_max_scale(numbers):
    low = min(numbers)
    high = max(numbers)
    
    # Handle the case where all numbers are the same
    if low == high:
        return [0.0 for _ in numbers]
        
    return [(x - low) / (high - low) for x in numbers]

# B = [2, 3, 1, 5, 4, 2, 8, 6, 7, 9, 0] # start
# B = generate_random_list(10000, lower_bound=0, upper_bound=100)
# B = generate_random_list(100, lower_bound=0, upper_bound=10000)
B = generate_random_list(100, lower_bound=0, upper_bound=10000)
B = [num * 100 for num in min_max_scale(B)]
"""
B = [2, 3, 1, 5, 4, 2, 8, 6, 7, 9, 0] # move left from idx 0 to 1
B = [2, 3, 1, 5, 4, 2, 8, 6, 7, 9, 0] # keep right in idx = len(B)-1 = 9
B = [2, 0, 1, 5, 4, 2, 8, 6, 7, 9, 3] # replace value in idx=1 to idx=9
B = [2, 0, 1, 5, 4, 2, 8, 6, 7, 9, 3] # move left from idx 1 to 3
B = [2, 0, 1, 5, 4, 2, 8, 6, 7, 9, 3] # move right from idx 9 to 2 (right<left -> CHANGE MID)
# mid = 2, left = 0 and right = 9
B = [2, 0, 1, 5, 4, 2, 8, 6, 7, 9, 3]
B = [0, 2, 1, 5, 4, 2, 8, 6, 7, 9, 3]
B = [0, 2, 1, 5, 4, 2, 8, 6, 7, 9, 3] # move right from idx 1 to 0; move left from 0 to 1 (right<left -> CHANGE MID)
# l=1, r=0
"""

#---------------------------------
# B = [0, 3, 1, 5, 4, 2, 8, 6, 7, 9, 2]
# B = [0, 1, 3, 5, 4, 2, 8, 6, 7, 9, 2]
#   [0, right=1, left=3, 5, 4, 2, 8, 6, 7, 9, 2]

# print(slow_sort_3(B))



# def slow_sort_4(A, old_mid=0):
def slow_sort_4(A, j=10):
    if not(leng := len(A)):
        return A
    elif not(mid := leng//2):
        return A

    equal = []
    smaller = []
    higher = []

    for i in range(0, leng):
        if A[i] < A[mid]:
            smaller.append(A[i])
        elif A[i] == A[mid]:
            equal.append(A[i])
        elif A[i] > A[mid]:
            higher.append(A[i])

    A = smaller + equal + higher
    # return slow_sort_4(A, A[mid]) if A[old_mid] != A[mid] else A
    j-=1
    return slow_sort_4(A, j) if j>=0 else A

A = [3, 9, 111, 5, 18, int((2**(1/2))*100), 77, 66, 1048, 0, 45_678]
# A = slow_sort_4(A, len(A)//2)
A = slow_sort_4(A, 10)
print(A)
B = generate_random_list(1000, lower_bound=0, upper_bound=1000)
# B = slow_sort_4(B, len(B)//2)
B = slow_sort_4(B, 995)
xpoints = np.array([idx for idx in enumerate(B)])
ypoints = np.array(B)

plt.plot(xpoints, ypoints)
plt.axis('off')
# plt.xticks(list(range(0, 101, 10)))
# plt.yticks([])
plt.show()
print(B)



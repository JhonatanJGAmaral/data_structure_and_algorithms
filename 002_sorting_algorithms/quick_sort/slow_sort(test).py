
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
def algo_test_3(list_to_sort):
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

test_slow_sort_2()

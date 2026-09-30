
def linear_search(A, T):
    assert isinstance(A, list), "A must be a list"
    for idx, val in enumerate(A):
        if val == T:
            return idx
    else:
        return -1

A = list(range(0, int(1e6), 7))
B = range(0, int(1e6), 7)

print(linear_search(A, 7))
print(linear_search(A, 7014))
print(linear_search(A, 350_168))
print(linear_search(A, 350_169))
print(linear_search(B, 14_738))

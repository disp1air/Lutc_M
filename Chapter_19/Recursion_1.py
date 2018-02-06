def recursionSum(L):
    print(L)
    if not L:
        return 0
    else:
        return L[0] + recursionSum(L[1:])

print(recursionSum([1, 2, 3, 4, 5]))

# косвенная рекурсия

def rec(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + rec(L[1:])

print(rec([1.1, 2.2, 3.3, 4.4]))
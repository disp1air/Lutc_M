# косвенная рекурсия

def rec(L):
    if not L: return 0
    return nonempty(L)

def nonempty(L):
    return L[0] + rec(L[1:])

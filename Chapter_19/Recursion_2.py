L = [1, [2, [3, 4], 5], 6, [7, 8]] # произвольно вложенные списки

def sumtree(L):
    total = 0
    for x in L:
        if not isinstance(x, list): 
            total += x
        else:
            total += sumtree(x)
    return total    

print(sumtree(L))
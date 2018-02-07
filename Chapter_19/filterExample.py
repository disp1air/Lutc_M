mylist = list(range(-5, 5))   # [-5, -4, -3, -2, -1, 0, 1, 2, 3, 4]

print(mylist)

print(list(filter((lambda x: x > 0), mylist)))
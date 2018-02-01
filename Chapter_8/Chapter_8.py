D = {'spam': 1, 'ham': 2, 'eggs': 4}

print(D['spam'])
print(D)

print(len(D))
print(D.keys())

D['ham'] = ['grill', 'bake', 'fry']
print(D)
# D = {'spam': 1, 'ham': ['grill', 'bake', 'fry'], 'eggs': 4}

del D['eggs']   # удаление элемента
print(D)

D['brunch'] = 'Bacon'   # добавление элемента
print(D)

X = [1, 2, 3]
Li = ['a', X, 'b'] # встроенная ссылка на объект Х
Di = {'x': X, 'y': 2}

# при изменении Х будут изменяться и Li и Di
# чтобы избежать этого сделаем копию Х
Li = ['a', X[:], 'b']
Di = {'x': X[:], 'y': 2}


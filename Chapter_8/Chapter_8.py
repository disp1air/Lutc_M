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

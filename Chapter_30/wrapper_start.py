from trace import Wrapper

x = Wrapper([1, 2, 3])   # обернуть список
x.append(4)              # делегировать операцию методу списка
print(x.wrapped)
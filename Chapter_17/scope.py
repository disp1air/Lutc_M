x = 99

def foo(y):
    z = x + y   # x - глобальная переменная
    return z

print(foo(1))
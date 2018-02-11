counters = [1, 2, 3, 4, 5]

def inc(x):
    return x + 10

# в версии 3.х функция map возвращает генератор
# поэтому приведем результат в удобный вид, т.е. к списку

print(list(map(inc, counters)))

print(list(map((lambda x: x + 100), counters)))
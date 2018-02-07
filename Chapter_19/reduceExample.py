from functools import reduce

sequence = list(range(1, 5))
print(sequence)

print(reduce((lambda x, y: x + y), sequence))
print(reduce((lambda x, y: x * y), sequence))

# реализация функции reduce
def myreduce(function, sequence):
    tally = sequence[0]
    for next in sequence[1:]:
        tally = function(tally, next)
    return tally

print(myreduce((lambda x, y: x + y), list(range(1, 5))))
print(myreduce((lambda x, y: x * y), list(range(1, 5))))
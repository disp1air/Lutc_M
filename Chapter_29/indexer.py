class Indexer:
    def __getitem__(self, index):
        return index ** 2

class Indexer_2:
    data = [5, 6, 7, 8, 9]

    def __getitem__(self, index):
        print('getitem_2: ', index)
        return self.data[index]

x = Indexer()
print(x[2])

y = Indexer_2()
print(y[0])
print(y[-1])

print(y[2:4])
print(y[::2])
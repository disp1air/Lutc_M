class C1:
    def __init__(self, who):   # создать имя при создании класса
        self.name = who

I1 = C1('Bob')   # создать два экземпляра I1, I2
I2 = C1('Jane')

print(I1.name)
print(I2.name
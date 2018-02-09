class C1:
    def setname(self, who):
        self.name = who

I1 = C1()   # создать два экземпляра I1, I2
I2 = C1()

I1.setname('Bob')
I2.setname('Jane')

print(I1.name)
print(I2.name)
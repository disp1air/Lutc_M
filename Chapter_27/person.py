# добавлен метод __str__ реализующий вывод объектов
class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

    def lastName(self):
        return self.name.split()[-1]
    
    def giveRaise(self, percent):
        self.pay = int(self.pay * (percent + 1))

    def __str__(self):
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus = .10):
        Person.giveRaise(self, percent + bonus)
    #    self.pay = int(self.pay * (1 + percent + bonus))

if __name__ == '__main__':   # когда файл запускается(самостоятельно) для тестирования
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)

    print(bob.name, bob.job, bob.pay)
    print(sue.name, sue.job, sue.pay)

    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue.pay)
    print(sue)

    tom = Manager('Tom Jones', 'mngr', 50000)
    tom.giveRaise(.10)
    print(tom.lastName())
    print(tom)

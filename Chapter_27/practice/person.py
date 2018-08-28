class Person:
  def __init__(self, name, job = None, pay = 0):
    self.name = name
    self.job = job
    self.pay = pay

  def lastName(self):
    print(self.name.split()[-1])

  def giveRaise(self, percent):
    self.pay *= percent

  def __str__(self):
    return '[Person: %s, %s]' % (self.name, self.pay)


class Manager(Person):
  def __init__(self, name, pay):
    Person.__init__(self, name, 'mng', pay)

  def giveRaise(self, percent, bonus=0.1):
    Person.giveRaise(self, percent + bonus)

if __name__ == '__main__':
  bob = Person('Bob Smith')
  sue = Person('Sue Jones', job = 'dev', pay = 100000)
  tom = Manager('Tom Soyer', 500000)

print(bob.name, bob.job, bob.pay)
print(tom.name, tom.job, tom.pay)
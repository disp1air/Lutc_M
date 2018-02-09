class Person:
    def __init__(self, name, job = None, pay = 0):
        self.name = name
        self.job = job
        self.pay = pay

if __name__ == '__main__':   # когда файл запускается(самостоятельно) для тестирования
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job = 'dev', pay = 100000)

    print(bob.name, bob.job, bob.pay)
    print(sue.name, sue.job, sue.pay) 
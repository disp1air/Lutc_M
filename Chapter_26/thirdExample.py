class FirstClass:
    def setdata(self, value):
        self.data = value

    def display(self):
        print(self.data)

class SecondClass(FirstClass):
    def display(self):
        print('Current value = "%s"' % self.data)

# Метод __add__ вызывается, когда экземпляр ThirdClass участвует в операции +
# Метод __str__ вызывается при выводе объекта (точнее, когда он преобразуется
#  в строку для вывода вызовом встроенной функции str или ее эквивалентом внутри интерпретатора).
class ThirdClass(SecondClass):
    def __init__(self, value):
        self.data = value

    def __add__(self, other):
        return ThirdClass(self.data + other)

    def __str__(self):
        return '[ThirdClass: %s]' % self.data

    def mul(self, other):
        self.data *= other
    
a = ThirdClass("abc")
a.display()
print(a)    # __str__ возвращает строку

b = a + 'xyz'   # новый __add__ : создается новый экземпляр
b.display()

print(b)

a.mul(3)
print(a)
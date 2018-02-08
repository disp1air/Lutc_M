Объект считается итерируемым, либо если он физически является последовательностью, либо если он является объектом, который воспроизводит по одному результату за раз в кон- тексте инструментов выполнения итераций, таких как цикл for.

                                    >>> for line in open(‘script1.py’): # Использовать итератор файла
                                        print(line.upper(), end=’’) # Вызывает метод __next__,
                                                                    # перехватывает исключение StopIteration
                                    IMPORT SYS
                                    PRINT(SYS.PATH)
                                    X = 2
                                    PRINT(2 ** 33)

Аргумент end='' в вызове функции print подавляет вывод символа \n, потому что строки, прочитанные из файла, уже содержат этот символ (если этот аргумент опустить, выводимые строки будут перемежаться пустыми строками).

С технической точки зрения итерационный протокол имеет еще одну сторону. В самом начале цикл for получает итератор из итерируемого объекта, передавая его встроенной функции iter, которая возвращает объект, имеющий требуемый метод next:

                                    >>> L = [1, 2, 3]
                                    >>> I = iter(L)    # Получить объект-итератор
                                    >>> I.__next__()   # Вызвать __next__, чтобы перейти к следующему элементу
                                    1
                                    >>> I.__next__()
                                    2
                                    >>> I.__next__()
                                    3
                                    >>> I.__next__()
                                    Traceback (most recent call last):
                                    ...текст сообщения об ошибке опущен...
                                    StopIteration

При работе с файлами этот начальный этап не нужен, потому что объект файла имеет собственный итератор. То есть объекты файлов имеют собственный метод next

Генераторы списков

                                    >>> L = [1, 2, 3, 4, 5]
                                    >>> L = [x + 10 for x in L]
                                    >>> L
                                    [21, 22, 23, 24, 25]
                                    
Выражения генераторов списков нельзя считать равнозначной заменой инструкции цикла for, потому что они создают новые объекты списков (что может иметь значение при наличии нескольких ссылок на первоначальный список), но это подходящая замена для большинства применений. Чтобы найти значение выражения, Python выполняет обход списка L, присваивая переменной x каждый очередной элемент, и собирает результаты, пропуская все элементы через выражение слева.
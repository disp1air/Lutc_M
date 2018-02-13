Сырые строки - в них спецсимволы никак не обрабатываются.

                    >>>print(r'hello \n world')
                    'hello \n world'
многострочные строки - используются три двойных кавычки(именно двойных, а не одинарных)

кортеж - неизменяемый тип данных, но если кортеж содержит список, то этот список изменять можно.

range(x, y) - создание последовательности

dir(object) - посмотреть список методов объекта dir(list), dir(dict)

help(object) - список методов с пояснениями help(list), help(dict)

namedtuple

type(type) type(object)

type и object - два базовых класса от которых все наследуется

модуль -> инструкции -> выражения -> объекты

функция id - уникальный идентификатор объекта(его адрес)

L2 is L1 # посути id(L2) == id(L1)

трехместное выражение if/else A = Y if X else Z

enumerate

s = 'spam' for (offset, item) in enumerate(s): print(item, 'appears at offset', offset)

s appears at offset 0 p appears at offset 1 a appears at offset 2 m appears at offset 3

сортировка: sorted - сортирует последовательность. исходная последовательность не изменится

менеджер контекста (with)

in - поиск в последовательности. возвращает True, False

утиная типизация

выражения-генераторы (i for i in range(5)) позволяют экономить память. следующий элемент можно вычислить из предыдущего к генератору можно сразу применять метод next()

модуль itertools

zip any() all()

ввод текста в консоли: i = input("text:")

форматированный вывод строк "qwerty {} ytrewq {}".format(3, 2) "qwerty {1} ytrewq {0}".format(2, 3) "qwerty {apple} ytrewq {banana}".format(apple=3,banana=2)

старый вариант "I have %i apples" % 2

open() открывает файл и возвращает "файл-подобный" объект f = open(text.txt)

чтение всего файла в одну строку f.read() f.seek(0) - перемещение указателя

чтение в список f.readlines()

работа с каждой строкой for line in open(text.txt): print(line.strip()) фун-ия open возвращает класс, этот класс может работать как итератор, т.е. при каждом вызове отдает по одной строке из файла

запись в файл f = open("test.txt", "w") f.write("Тест") печатать в файл print("text", file=f)

встроенные функции языка min, len, any

module copy copy.copy() copy.deepcopy()

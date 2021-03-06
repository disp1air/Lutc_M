В действительности термин "перегрузка операторов" означает всего лишь перехватывание встроенных операций с помощью методов классов – интерпретатор автоматически вызывает эти методы при выполнении встроенных операций над экземплярами классов, а методы должны возвращать значения, которые будут интерпретироваться как результаты соответствующих операций.  

Другими словами, если в классе определен метод со специальным именем, интерпретатор автоматически будет вызывать его при выполнении соответствующей методу операции над экземплярами этого класса.  

Например, по определению языка оператор + всегда отображается на имя \__add__ независимо от того, что в действительности делает метод \__add__.

Методы перегрузки операторов могут наследоваться от суперклассов, если они отсутствуют в самом классе, как и любые другие методы. Кроме того, методы перегрузки операторов являются необязательными – если какой-то метод не
реализован, это лишь означает, что соответствующая ему операция не поддерживается классом, а при попытке применить такую операцию возбуждается исключение.  

Когда экземпляр X появляется в выражении извлечения элемента по индексу, таком как X[i], интерпретатор Python вызывает метод \_\_getitem__, наследуемый этим экземпляром, передавая методу объект X в первом аргументе и индекс, указанный в квадратных скобках, во втором аргументе.

                                    >>> class Indexer:
                                            def __getitem__(self, index):
                                                return index ** 2

                                    >>> X = Indexer()
                                    >>> X[2]
                                    4  

                                    >>> for i in range(5):
                                        print(X[i], end=' ') # Вызывает __getitem__(X, i) в каждой итерации

                                    0 1 4 9 16

Метод \_\_getitem__ вызывается не только при выполнении операции обращения к элементу по индексу, но и при извлечении срезов.

Однако в действительности параметры среза определяются с помощью объекта среза, который и передается реализации операции индексирования списка. Фактически вы всегда можете передать объект среза вручную – синтаксис срезов в значительной степени является всего лишь синтаксическим подсластителем для операции индексирования с применением объекта среза:

                    >>> L[slice(2, 4)] # Извлечение среза с помощью объекта среза. Аналогично L[2:4]
Пример для перегрузки операторов с возможностью извлечения срезов:

                                class Indexer_2:
                                    data = [5, 6, 7, 8, 9]

                                    def __getitem__(self, index):
                                        print('getitem_2: ', index)
                                        return self.data[index]

                                >>> X = Indexer()
                                >>> X[0] 
                                getitem: 0 
                                5

                                >>> X[2:4] # При извлечении среза __getitem__ получает объект среза
                                getitem: slice(2, 4, None)
                                [7, 8]

Инструкция for многократно применяет операцию индексирования к последовательности, используя индексы от нуля и выше, пока не будет получено исключение выхода за границы. Благодаря этому метод \_\_getitem__ представляет собой один из способов перегрузки итераций в языке Python – если этот метод реализован, инструкции циклов for будут вызывать его на каждом шаге цикла, с постоянно увеличивающимся значением смещения.

                                >>> class stepper:
                                    def __getitem__(self, i):
                                        return self.data[i]

                                >>> X = stepper()
                                >>> X.data = 'Spam'

                                >>> X[1] # Индексирование, вызывается __getitem__
                                'p'

                                >>> for item in X: # Циклы for вызывают __getitem__
                                        print(item, end=' ') # Инструкция for индексирует элементы 0..N

                                S p a m  

Любой класс, поддерживающий циклы for, автоматически поддерживает все итерационные контексты, имеющиеся в языке Python. Например, оператор проверки на принадлежность in, генераторы списков, встроенная функция map, присваивание списков и кортежей и конструкторы типов также автоматически вызывают метод \__getitem__,
если он определен:  

                                >>> 'p' in X # Во всех этих случаях вызывается __getitem__
                                True  

                                >>> [c for c in X] # Генератор списков
                                ['S', 'p', 'a', 'm']

                                >>> list(map(str.upper, X)) # Функция map (в версии 3.0
                                ['S', 'P', 'A', 'M'] # требуется использовать функцию list)

                                >>> (a, b, c, d) = X # Присваивание последовательностей
                                >>> a, c, d
                                ('S', 'a', 'm')

                                >>> list(X), tuple(X), ''.join(X)
                                (['S', 'p', 'a', 'm'], ('S', 'p', 'a', 'm'), 'Spam')

                                >>> X
                                <__main__.stepper instance at 0x00A8D5D0>

В настоящее время все итерационные контексты в языке Python пытаются сначала использовать метод \_\_iter\_\_, и только потом – метод \_\_getitem__. То есть при выполнении обхода элементов объекта предпочтение отдается итерационному протоколу - если итерационный протокол не поддерживается объектом, вместо него используется операция
индексирования.  

С технической точки зрения итерационные контексты вызывают встроенную функцию iter, чтобы определить наличие метода \__iter__, который должен возвращать объект итератора. Если он предоставляется, то интерпретатор Python
будет вызывать метод \__next__ объекта итератора для получения элементов до тех пор, пока не будет возбуждено исключение StopIteration. Если метод \__iter__ отсутствует, интерпретатор переходит на использование схемы с применением метода \__getitem__ и начинает извлекать элементы по индексам, пока не будет возбуждено исключение IndexError. Кроме того, для удобства предоставляется встроенная функция next, позволяющая выполнять итерации вручную: вызов next(I) – это то же самое, что вызов I.\__next__().  

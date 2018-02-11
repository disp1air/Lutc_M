Подобно инструкции def, инструкция class создает объект и является неявной инструкцией присваивания – когда она выполняется, создается объект класса, ссылка на который сохраняется в имени, использованном в заголовке инструкции.

                                    class NextClass:
                                        def printer(self, text):
                                            self.message = text
                                            print(self.message)

                                    >>> x = NextClass()
                                    >>> x.printer('instance call')        

Когда метод вызывается с использованием квалифицированного имени экземпляра, как в данном случае, то сначала определяется местонахождение метода printer, а затем его аргументу self автоматически присваивается объект экземпляра (x). В аргумент text записывается строка, переданная в вызов метода ('instance call').

Методы могут вызываться любым из двух способов – через экземпляр или через сам класс. Например, метод printer может быть вызван с использованием имени класса, при этом ему явно требуется передать экземпляр в аргументе self:

                                    >>> NextClass.printer(x, 'class call') # Прямой вызов метода класса
                                    class call

Вызов метода, который производится через экземпляр и через имя класса, оказывает одинаковое воздействие при условии, что при вызове через имя класса передается тот же самый экземпляр. По умолчанию, если попытаться вызвать
метод без указания экземпляра, будет выведено сообщение об ошибке:

                                    >>> NextClass.printer('bad call')
                                    TypeError: unbound method printer() must be called with NextClass instance...

Приемы организации взаимодействия классов

                                    class Super:
                                        def method(self):
                                            print('in Super.method') # Поведение по умолчанию
                                        
                                        def delegate(self):
                                            self.action()            # Ожидаемый метод

                                    class Inheritor(Super): # Наследует методы, как они есть
                                        pass

                                    class Replacer(Super): # Полностью замещает method
                                        def method(self):
                                            print('in Replacer.method')

                                    class Extender(Super): # Расширяет поведение метода method
                                        def method(self):
                                            print('starting Extender.method')
                                            Super.method(self)
                                            print('ending Extender.method')

                                    class Provider(Super): # Определяет необходимый метод
                                        def action(self):
                                            print('in Provider.action')

Когда через экземпляр класса Provider вызывается метод delegate, инициируются две независимые процедуры поиска:
1. При вызове x.delegate интерпретатор отыскивает метод delegate в классе Super, начиная поиск от экземпляра класса Provider и двигаясь вверх по дереву наследования. Экземпляр x передается методу в виде аргумента self, как обычно.
2. Внутри метода Super.delegate выражение self.action приводит к запуску нового, независимого поиска в дереве наследования, начиная от экземпляра self и дальше вверх по дереву. Поскольку аргумент self ссылается на экземпляр класса Provider, метод action будет найден в подклассе Provider.

Пространства имен модулей фактически реализованы как словари и доступны в виде встроенного атрибута /_/_dict/_/_. То же относится к объектам классов и экземпляров: обращение к квалифицированному имени атрибута фактически является операцией доступа к элементу словаря, а механизм наследования атрибута работает лишь как поиск в связанных словарях.

                                    >>> class super:
                                            def hello(self):
                                                self.data1 = 'spam'

                                    >>> class sub(super):
                                            def hola(self):
                                                self.data2 = 'eggs'

Когда мы создаем экземпляр подкласса, он начинает свое существование с пустым словарем пространства имен, но имеет ссылку на класс, стоящий выше в дереве наследования. Фактически дерево наследования доступно в виде специальных атрибутов. Экземпляры обладают атрибутом /_/_class/_/_, который ссылается на класс, а классы имеют атрибут
/_/_bases/_/_, который является кортежем, содержащим ссылки на суперклассы выше в дереве наследования.

                                    >>> x = sub()
                                    >>> x./_/_dict/_/_                 # словарь пространства имен экземпляра
                                    {}

                                    >>> x./_/_class/_/_                # класс экземпляра
                                    <class '/_/_main/_/_.sub'>

                                    >>> sub./_/_bases/_/_              # суперклассы данного класса
                                    (<class '/_/_main/_/_.super'>,)

                                    >>> super./_/_bases/_/_
                                    (<class 'object'>,)

                                    >>> X.hello()
                                    >>> X./_/_dict/_/_
                                    {'data1': 'spam'}

                                    >>> X.hola()
                                    >>> X./_/_dict/_/_
                                    {'data1': 'spam', 'data2': 'eggs'}
                                    >>> sub./_/_dict/_/_.keys()
                                    ['/_/_module/_/_', '/_/_doc/_/_', 'hola']
                                    >>> super./_/_dict/_/_.keys()
                                    ['/_/_dict/_/_', '/_/_module/_/_', '/_/_weakref/_/_', 'hello', '/_/_doc/_/_'>]

Так как атрибуты фактически являются ключами словаря, существует два способа получать и изменять их значения – по квалифицированным именам или индексированием по ключу:

                                    >>> X.data1, X./_/_dict/_/_['data1']
                                    ('spam', 'spam')

                                    >>> X.data3 = 'toast'
                                    >>> X./_/_dict/_/_
                                    {'data1': 'spam', 'data3': 'toast', 'data2': 'eggs'}

                                    >>> X./_/_dict/_/_['data3'] = 'ham'
                                    >>> X.data3
                                    'ham'

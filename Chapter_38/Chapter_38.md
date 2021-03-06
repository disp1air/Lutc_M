**Что такое декоратор**  
Декорирование - способ управления функциями и классами. Сами декораторы имеют форму вызываемых объектов (таких, как функции), которые обрабатывают другие вызываемые объекты.  

Декораторы в языке Python имеют две родственные разновидности:  
 - **декораторы функций** связывают имя функции с другим вызываемым объектом на этапе определения функции, добавляя дополнительный уровень логики, которая управляет функциями и методами или выполняет некоторые действия в случае их вызова.
 - **Декораторы классов** связывают имя класса с другим вызываемым объектом на этапе его определения, добавляя дополнительный уровень логики, которая управляет классами или экземплярами, созданными при обращении к этим классам.

В двух словах, декораторы предоставляют возможность в конце инструкции def определения функции в случае декораторов функций или в конце инструкции class определения класса в случае декораторов классов добавить автоматически вызываемый программный код. Этот программный код может служить самым разным целям.  

Например, в типичном случае, автоматически запускаемый программный код может использоваться для выполнения дополнительных операций при вызове функций и классов. Для достижения этой цели устанавливается объект-обертка, который вызывается позднее:
 - Декораторы функций устанавливают объекты-обертки, перехватывающие вызовы функций и выполняющие необходимые операции.
 - Декораторы классов устанавливают объекты-обертки, перехватывающие попытки создания экземпляров и выполняющие необходимые операции.  

Этот эффект достигается декораторами автоматически, за счет автоматического связывания имен функций и классов с другими вызываемыми объектами в конце инструкций def и class. При последующих вызовах эти вызываемые объекты могут выполнять самые разные операции, такие как трассировка и хронометраж вызовов функций, управление доступом к атрибутам экземпляров классов и так далее.  

Декораторы функций могут также управлять не только вызовами функций, но и самими объектами функций, например регистрировать функции в некотором прикладном интерфейсе.  

основное волшебство декораторов сводится к автоматической операции повторного присваивания.

**Основы декораторов функций**  
Декораторы в значительной степени являются всего лишь синтаксическим подсластителем – конструкцией, которая передает одну функцию в вызов другой в конце инструкции def и присваивает результат оригинальному имени первой функции.

Декораторы функций являются своего рода объявлениями времени выполнения для функций, определения которых следуют за декораторами. Декоратор указывается в отдельной строке непосредственно перед инструкцией def, определяющей функцию и состоит из символа @, за которым следует имя метафункции – функции (или другого вызываемого объекта), управляющей
другой функцией.  

С точки зрения программирования, декоратор функции автоматически отображает следующую конструкцию:

                              @decorator # Декорирование функции
                              def F(arg):
                                ...
                              F(99) # Вызов функции  

в эквивалентную ей форму, где decorator – это вызываемый объект, принимающий единственный аргумент и возвращающий вызываемый объект, который принимает тот же набор аргументов, что и оригинальная функция F:  

                              def F(arg):
                                ...
                              F = decorator(F) # Присваивает имени функции результат вызова декоратора
                              F(99) # Фактически вызывается decorator(F)(99)

Такое автоматическое повторное присваивание имени оригинальной функции может применяться к любым инструкциям def, будь то определение обычной функции или определение метода внутри инструкции class. Когда позднее производится вызов функции F, фактически вызывается объект, возвращаемый декоратором, который может быть или другим объектом, реализующим необходимую логику, обертывающую логику оригинальной функции, или самой оригинальной функцией.

Другими словами, декорирование по сути заключается в отображении первого вызова из следующих ниже во второй (при том, что декоратор в действительности вызывается только один раз – на этапе декорирования):

                              func(6, 7)
                              decorator(func)(6, 7)

Такое автоматическое повторное связывание имени объясняет синтаксис объявления статических методов и свойств, который мы видели ранее в книге:

                              class C:
                                @staticmethod
                                def meth(...): ... # meth = staticmethod(meth)

                              class C:
                                @property
                                def name(self): ... # name = property(name)

В обоих случаях в конце инструкции def имени метода присваивается результат вызова встроенного декоратора. Вызов оригинального имени позднее приведет к вызову объекта, который вернул декоратор.

Декоратор сам по себе является вызываемым объектом, который возвращает вызываемый объект. То есть он возвращает объект, который будет вызываться при вызове декорируемой функции по ее оригинальному имени, – это может быть объект-обертка, перехватывающий вызовы оригинальной функции, или сама оригинальная функция, дополненная новыми возможностями.  

Например, чтобы понять, как действует протокол декорирования, позволяющий организовать управление функциями сразу после их создания, можно создать декоратор, имеющий следующий вид:

                              def decorator(F):
                                Обработка функции F
                                return F

                              @decorator
                              def func(): ... # func = decorator(func)

Поскольку имени функции опять присваивается оригинальная функция, этот декоратор просто выполняет некоторые действия после определения функции. Такие декораторы могут использоваться для регистрации функций в прикладном интерфейсе, для присоединения атрибутов к функциям и тому подобного.  

Ниже приводится типичный шаблон построения декоратора, демонстрирующий эту идею, – декоратор возвращает обертку, которая сохраняет оригинальную функцию в области видимости объемлющей функции:

                              def decorator(F): # На этапе декорирования @
                                def wrapper(*args): # Обертывающая функция
                                // Использование F и аргументов
                                // F(*args) – вызов оригинальной функции
                              return wrapper

                              @decorator # func = decorator(func)
                              def func(x, y): # func передается декоратору в аргументе F
                                ...

                              func(6, 7) # 6, 7 передаются функции wrapper в виде *args

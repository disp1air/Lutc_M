Синтаксическое правило состоит в том, что все инструкции в пределах одного блока должны иметь один и тот же отступ от левого края. Если это не так, будет получена синтаксическая ошибка, и программный код не будет работать, пока не исправить отступ.

                                    if x > y:
                                        x = 3
                                        y = 5

!!! ввод пользователя всегда передается сценарию в виде строки

**Несколько специальных случаев**
Обычно на каждой строке располагается одна инструкция, но вполне возможно для большей компактности записать несколько инструкций в одной строке, разделив их точками с запятой:  

                    a = 1; b = 2; print(a + b) # Три инструкции на одной строке

Это единственный случай, когда в языке Python необходимо использовать точки с запятой: как разделители инструкций. Однако такой подход не может применяться к составным инструкциям. Другими словами, в одной строке можно размещать только простые инструкции, такие как присваивание, print и вызовы функций. Составные инструкции по-прежнему должны находиться в отдельной строке(иначе всю программу можно было бы записать в одну строку).  

допускается записывать одну инструкцию в нескольких строках. Для этого достаточно заключить часть инструкции в пару
скобок – круглых (()), квадратных ([]) или фигурных ({}). Любой программный код, заключенный в одну из этих конструкций, может располагаться на нескольких строках: инструкция не будет считаться законченной, пока интерпретатор Python не достигнет строки с закрывающей скобкой. Например, литерал списка можно записать так:  

                                            mlist = [111,
                                                    222,
                                                    333]

Отступы в строках, где продолжается инструкция, в учет не принимаются, хотя здравый смысл диктует, что строки все-таки должны иметь некоторые отступы для обеспечения удобочитаемости.

Круглые скобки являются самым универсальным средством, потому что в них можно заключить любое выражение. Добавьте левую скобку, и вы сможете перейти на следующую строку и продолжить свою инструкцию:

                                            X = (A + B +
                                                 C + D)

Между прочим, такой прием допускается применять и к составным инструкциям. Если вам требуется записать длинное выражение, оберните его круглыми скобками и продолжите на следующей строке:

                                            if (A == 1 and
                                                B == 2 and
                                                C == 3):
                                                    print(‘spam’ * 3)  

Специальный случай: тело составной инструкции может располагаться в той же строке, что и основная инструкция, после символа двоеточия:

                                            if x > y: print(x)

Это позволяет записывать в одной строке условные операторы, циклы и так далее. Однако такой прием будет работать, только если тело составной инструкции не содержит других составных инструкций. То есть после двоеточия могут следовать только простые инструкции – инструкции присваивания, инструкции print, вызовы функций и подобные им. Крупные инструкции по-прежнему
должны записываться в отдельных строках.  

                                            while True:
                                                reply = input('Enter text: ')
                                                if reply == 'stop': break
                                                print(reply.upper())

Обработка ошибок с помощью инструкции try

                                            while True:
                                                reply = input(‘Enter text:’)
                                                if reply == ‘stop’: break
                                                try:
                                                    num = int(reply)
                                                except:
                                                    print(‘Bad!’ * 8)
                                                else:
                                                    print(int(reply) ** 2)
                                            print ‘Bye’


Чтобы возбудить исключение вручную, достаточно просто выполнить инструкцию raise.

try: raise IndexError # Возбуждает исключение вручную except IndexError: print('got exception')

got exception  

Если исключение, определяемое программой, не перехватывается, оно будет передано обработчику исключений по умолчанию, что приведет к завершению программы с выводом стандартного сообщения об ошибке:  

                                    >>> raise IndexError
                                    Traceback (most recent call last):
                                    File “<stdin>”, line 1, in <module>
                                    IndexError

вы также можете определять новые исключения для внутренних нужд своих программ. Пользовательские исключения создаются в виде классов, наследующих один из классов встроенных исключений, – обычно класс с именем Exception.  

                                    class Bad(Exception):
                                        pass

                                    def doomed():
                                        raise Bad()

                                    try:
                                        doomed()
                                        except Bad:
                                        print(‘got Bad’)

                                    got Bad


Чтобы возбудить исключение вручную, достаточно просто выполнить инструкцию raise.

try: raise IndexError # Возбуждает исключение вручную except IndexError: print('got exception')

got exception
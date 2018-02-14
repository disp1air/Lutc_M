def fetcher(obj, index):
    return obj[index]

x = 'spam'

def catcher():
    try:
        fetcher(x, 4)
    except IndexError:
        print('got exception!')
    print('continuing')

catcher()

try:
    raise IndexError   # возбуждает исключение вручную
except IndexError:
    print('got exception')
def after():
    try:
        raise IndexError
    finally:
        print('finally block')
    print('after try')

after()

def combine_all():
    try:
        raise IndexError
    except IndexError:
        print('Except block')
    finally:
        print('finally block')
    print('global block')

combine_all()
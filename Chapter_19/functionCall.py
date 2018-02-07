def echo(message):
    print(message)

def indirect(func, arg):
    func(arg)

indirect(echo, 'Argument call')

schedule = [ (echo, 'Spam!'), (echo, 'Ham!') ]

for (func, arg) in schedule:
    func(arg)

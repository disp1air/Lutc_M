class Wrapper:
    def __init__(self, object):
        self.wrapped = object

    def __getattr__(self, attrname):
        print('Trace:', attrname)              # отметить факт извлечения 
        return getattr(self.wrapped, attrname) # делегировать извлечение
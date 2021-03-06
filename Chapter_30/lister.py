class ListInstance:
    """
    Примесный класс, реализующий получение форматированной строки при вызове
    функций print() и str() с экземпляром в виде аргумента, через наследование
    метода __str__, реализованного здесь; отображает только атрибуты
    экземпляра; self – экземпляр самого нижнего класса в дереве наследования;
    во избежание конфликтов с именами атрибутов клиентских классов использует
    имена вида __X
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, 
            id(self),
            self.__attrnames()
        )
    
    def __attrnames(self):
        result = ''
        for attr in sorted(self.__dict__):
            result += '\tname %s=%s\n' % (
                attr, self.__dict__[attr]
            )
        return result


class ListInherited:
    """
    Использует функцию dir() для получения списка атрибутов самого экземпляра
    и атрибутов, унаследованных экземпляром от его классов; в Python 3.0
    выводится больше имен атрибутов, чем в 2.6, потому что классы нового стиля
    в конечном итоге наследуют суперкласс object; метод getattr() позволяет
    получить значения унаследованных атрибутов, отсутствующих в self.__dict__;
    реализует метод __str__, а не __repr__, потому что в противном случае
    данная реализация может попасть в бесконечный цикл при выводе связанных
    методов!    
    """

    def __str__(self):
        return '<Instance of %s, address %s:\n%s>' % (
            self.__class__.__name__, 
            id(self),
            self.__attrnames()
        )

    def __attrnames(self):
        result = ''
        for attr in dir(self):
            if attr[:2] == '__' and attr[-2:] == '__'
                result += '\tname %s=<>\n' % attr
            else:
                result += '\tname %s=%s\n' % (attr, getattr(self, attr))
        return result
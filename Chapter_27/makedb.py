from person import Person, Manager

bob = Person('Bob Clinton')
thomas = Person('Thomas Jeb', job = 'dev', pay = 100000)
sarah = Manager('Sarah Parker', 50000)

import shelve
db = shelve.open('persondb')      # имя файла хранилища

for obj in (bob, thomas, sarah):
    db[obj.name] = obj
db.close()                        # закрыть после внесения изменений
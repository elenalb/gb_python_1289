# модификаторы доступа

# public - публичный - info
# protected - защищенный - _info
# private - приватный - __info


class Auto:
    def __init__(self):
        print("Автомобиль заведен")
        self.auto_name = "Audi"
        self._auto_model = "007"
        self.__auto_year = 2020


# a = Auto()
# print(a.auto_name)
# print(a._auto_model)
# print(a.__auto_year)

# инкапсуляция
class MyClass:
    _attr = "value"

    def _method(self):
        print("Это защищенный метод!")


mc = MyClass()
mc._method()
print(mc._attr)


class MyClass1:
    __attr = "value"

    def __method(self):
        print("Это приватный ветод!")


mc1 = MyClass1()
# _ИмяКласса__имя_атрибута
mc1._MyClass1__method()
print(mc1._MyClass1__attr)

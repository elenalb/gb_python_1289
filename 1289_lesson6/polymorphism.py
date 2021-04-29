# Полиморфизм


# перегрузка методов
class MyClass:
    def my_method(self, param1, param2=None):
        if param2:
            print(param1 + param2)
        else:
            print(param1)


mc = MyClass()
mc.my_method(1)
mc.my_method(1, 2)


# переопределение методов
class Transport:
    def show_info(self):
        print("Класс Transport")


class Auto(Transport):
    def show_info(self):
        print("Класс Auto")


class Bus(Transport):
    def show_info(self):
        print("Класс Bus")


t = Transport()
t.show_info()
a = Auto()
a.show_info()
b = Bus()
b.show_info()

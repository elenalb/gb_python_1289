# статические методы
# @staticmethod


class Auto:
    @staticmethod
    def get_class_info():
        print("Детальная информация о классе Auto")


Auto.get_class_info()


class MyClass:
    @staticmethod
    def sum_1(param1, param2):
        return param1 + param2

    def sum_2(self, param1, param2):
        return param1 + param2

    def sum_3(self, param1, param2):
        return MyClass.sum_1(param1, param2)


# print(MyClass.sum_1(1, 2))
# mc = MyClass()
# print(mc.sum_2(1, 2))
# print(mc.sum_1(1, 2))
# print(mc.sum_3(1, 2))


# методы класса
# @classmethod


class MyClass1:
    @classmethod
    def my_method(cls, param):
        print(cls, param)


MyClass1.my_method('hello')
mc = MyClass1()
mc.my_method('hello')

# open("file", "w", encoding="utf-8")

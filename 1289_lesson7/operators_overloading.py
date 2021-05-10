# перегрузка операторов
# __init__() - конструктор
# __del__() - деструктор
# __str__() - print()
# __add__() - +
# __setattr__() - =
# __getitem__() - взятие по индексу
# __call__() - обращение к экземпляру как к функции
# __gt__() - >
# __lt__() - <
# __ge__() - >=
# __le__() - <=
# __eq__() - ==
# __iadd__() - +=
# __isub__() - -=


# __init__()
class MyClass:
    def __init__(self, param):
        self.param = param

# [[1, 2, 3], [2, 3, 4], [2, 3, 5]]
# 1 2 3   2 3 4   3 5 7
# 2 3 4 + 2 4 7 = 4 7 11
# 2 3 5   6 5 4   8 8 9


mc = MyClass("param")
print(mc.param)


# __del__()
# class MyClass:
#     def __init__(self, param):
#         self.param = param
#
#     def __del__(self):
#         print(f"Удаляем объект {self.param} класса MyClass")
#
#
# mc = MyClass("param")
# del mc
# print(mc.param)  # mc удален!

# __str__()
# class MyClass:
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#
#     def __str__(self):
#         return f"Объект с параметрами {self.param1} и {self.param2}"
#
#
# mc = MyClass(1, 2)
# print(mc)

# # __add__()
# class MyClass:
#     def __init__(self, digit1, digit2):
#         self.digit1 = digit1
#         self.digit2 = digit2
#
#     def __add__(self, other):
#         return MyClass(self.digit1 + other.digit1, self.digit2 + other.digit2)
#
#     def __str__(self):
#         return f"Объект с параметрами {self.digit1} и {self.digit2}"
#
#
# mc1 = MyClass(1, 2)
# mc2 = MyClass(3, 4)
# print(mc1 + mc2)


# # __setattr__()
# class MyClass:
#     def __setattr__(self, key, value):
#         if key == "width":
#             self.__dict__[key] = value
#         else:
#             print(f"Атрибут {key} недопустим!")
#
#
# mc = MyClass()
# mc.height = 40


# # __eq__()
# class MyClass:
#     def __init__(self):
#         self.x = 10
#
#     def __eq__(self, y):
#         return self.x == y
#
#
# mc = MyClass()
# print("Равно" if mc == 10 else "Не равно")
# print("Равно" if mc == 11 else "Не равно")

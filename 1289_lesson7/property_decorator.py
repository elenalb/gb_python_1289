# декоратор @property


# class MyClass:
#     def __init__(self, param1, param2):
#         self.param1 = param1
#         self.param2 = param2
#
#     @property
#     def my_method(self):
#         return f"Параметры класса MyClass: {self.param1}, {self.param2}"
#
#
# mc = MyClass("param1", "param2")
# print(mc.param1)
# print(mc.my_method)


class Auto:
    def __init__(self, year):
        self.year = year

    @property
    def year(self):
        return self.__year

    @year.setter
    def year(self, year):
        if year < 2000:
            self.__year = 2000
        elif year > 2020:
            self.__year = 2020
        else:
            self.__year = year

    def get_auto_year(self):
        return f"Автомобиль выпущен в {self.year} году"


a = Auto(1996)
print(a.get_auto_year())

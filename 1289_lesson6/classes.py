# класс, объект, атрибут


class Auto:
    # атрибуты класса
    auto_name = "Audi"
    auto_model = "007"
    auto_year = 2020

    # методы класса
    def auto_start(self):
        print("Заводим автомобиль")

    def auto_stop(self):
        print("Останавливаем работу двигателя")


# # объект / экземпляр класса
# a = Auto()
# print(a)
# print(a.auto_name)
# print(a.auto_start())
# print(a.auto_stop())

class Auto1:
    # атрибуты класса
    auto_count = 0

    # методы класса
    def auto_start(self, auto_name, auto_model, auto_year):
        # атрибуты экземпляра
        self.auto_name = auto_name
        self.auto_model = auto_model
        self.auto_year = auto_year
        Auto1.auto_count += 1


a1 = Auto1()
a1.auto_start("Audi", "007", "2020")
print(a1.auto_count)
print(a1.auto_name)
a2 = Auto1()
a2.auto_start("Mazda", "CX", "2019")
print(a2.auto_count)
print(a2.auto_name)

# наследование


class Transport:
    def transport_method(self):
        print("Родительский метод")


class Auto(Transport):
    def auto_method(self):
        print("Это дочерний метод класса Auto")


class Bus(Transport):
    def bus_method(self):
        print("Это дочерний метод класса Bus")


# a = Auto()
# a.transport_method()
# a.auto_method()
# b = Bus()
# b.transport_method()
# b.bus_method()


class Shape:
    def __init__(self, color, param1, param2):
        self.color = color
        self.param1 = param1
        self.param2 = param2

    def square(self):
        return self.param1 * self.param2


class Rectangle(Shape):
    def __init__(self, color, param1, param2):
        super().__init__(color, param1, param2)

    def get_r_p(self):
        return 2 * (self.param1 + self.param2)


class Squre(Shape):
    def __init__(self, color, param):
        Shape.__init__(self, color, param, param)

    def get_s_p(self):
        return 4 * self.param1


# r = Rectangle("white", 1, 2)
# print(r.square())
# print(r.get_r_p())
# print(r.color)
# s = Squre("black", 2)
# print(s.square())
# print(s.get_s_p())
# print(s.color)


class Player:
    def method(self):
        print("Родительский метод класса Player")

    def player_method(self):
        print("Родительский метод класса Player")


class Navigator:
    def method(self):
        print("Родительский метод класса Navigator")

    def navigator_method(self):
        print("Родительский метод класса Navigator")


class MobilePhone(Navigator, Player):
    def mobile_phone_method(self):
        print("Дочерний метод класса MobilePhone")


mp = MobilePhone()
mp.player_method()
mp.navigator_method()
mp.mobile_phone_method()
mp.method()

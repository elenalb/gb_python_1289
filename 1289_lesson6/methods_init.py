# конструкторы, методы класса


class Auto:
    auto_count = 0

    def __init__(self):
        Auto.auto_count += 1
        print(Auto.auto_count)

    def get_class_info(self):
        print(f"Детальная информация о классе: количество экземпляров класса {Auto.auto_count}")


a1 = Auto()
a2 = Auto()
a3 = Auto()
a1.get_class_info()

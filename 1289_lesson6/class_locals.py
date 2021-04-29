# локальные переменные


class Auto:
    # глобальная переменная
    info_1 = "Класс Auto"

    def auto_start(self):
        # локальная переменная
        info = "Автомобиль заведен"
        return info


a = Auto()
# print(a.info)
info = a.auto_start()
print(info)
print(a.info_1)

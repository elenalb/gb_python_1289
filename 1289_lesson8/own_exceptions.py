# создание собственных исключений

try:
    print(100/1)
except ZeroDivisionError:
    print("Делить на ноль нельзя!")
else:
    print("Все отлично!")
finally:
    print("Программа завершена")


class OwnError(Exception):
    def __init__(self, txt):
        self.txt = txt


input_data = input("Введите положительное число: ")
try:
    input_data = int(input_data)
    if input_data < 0:
        raise OwnError("Вы ввели отрицательное число!")
except ValueError:
    print("Вы ввели не число!")
except OwnError as err:
    print(err)
else:
    print(f"Вы ввели число {input_data}")


import traceback


def division(a, b):
    return a / b


try:
    res = division(1, 0)
except Exception as e:
    print(f'Ошибка:\n {traceback.format_exc()}')

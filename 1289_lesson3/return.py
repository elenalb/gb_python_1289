# оператор return


# return со значением
def s_calc():
    r_val = float(input("Введите радиус цилиндра: "))
    h_val = float(input("Введите высоту цилиндра: "))
    # площадь боковой поверхности
    s_side = h_val * 2 * 3.14 * r_val
    # площадь оснований
    s_circle = 2 * 3.14 * r_val ** 2
    # полная площадь
    s = s_side + s_circle
    return s


# s_val = s_calc()
# print(s_val)
# print(s_calc())


# return без значения
def s_calc_1():
    try:
        r_val = float(input("Введите радиус цилиндра: "))
        h_val = float(input("Введите высоту цилиндра: "))
    except ValueError:
        print("Вы ввели не числа!")
        return
    # площадь боковой поверхности
    s_side = h_val * 2 * 3.14 * r_val
    # площадь оснований
    s_circle = 2 * 3.14 * r_val ** 2
    # полная площадь
    s = s_side + s_circle
    return round(s, 2)


# print(s_calc_1())


def print_message(message):
    print(message)


# DRY - don't repeat yourself
print(print_message('Hello!'))


# возврат набора значений
def s_calc_2():
    try:
        r_val = float(input("Введите радиус цилиндра: "))
        h_val = float(input("Введите высоту цилиндра: "))
    except ValueError:
        print("Вы ввели не числа!")
        return
    # площадь боковой поверхности
    s_side = h_val * 2 * 3.14 * r_val
    # площадь оснований
    s_circle = 3.14 * r_val ** 2
    # полная площадь
    s = s_side + 2 * s_circle
    return s, s_side, s_circle


# first_s = s_calc_2()
# print(first_s)
#
# s_val, s_side, s_circle = s_calc_2()
# print(f"Площадь цилиндра: {s_val}, площадь боковой поверхности: {s_side}")

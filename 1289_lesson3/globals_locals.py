# области видимости переменных
# локальная, глобальная, нелокальная


# локальная область видимости
def s_calc(r_val, h_val):
    # площадь боковой поверхности
    s_side = h_val * 2 * 3.14 * r_val
    # площадь оснований
    s_circle = 2 * 3.14 * r_val ** 2
    # полная площадь
    s = s_side + s_circle
    return s

#
# s_val = s_calc(10, 10)
# print(s_val)


s_side = None
s_circle = None


# глобальная область видимости
def s_calc_1(r_val, h_val):
    global s_side, s_circle
    # площадь боковой поверхности
    s_side = h_val * 2 * 3.14 * r_val
    # площадь оснований
    s_circle = 2 * 3.14 * r_val ** 2
    # полная площадь
    s = s_side + s_circle
    return s


# s_val_1 = s_calc_1(10, 10)
# print(s_val_1)
# print(s_side)
# print(globals())


# нелокальная область видимости
def ext_func():
    my_var = 0

    def int_func():
        nonlocal my_var
        my_var += 1
        return my_var

    return int_func


f_obj = ext_func()
print(f_obj)
print(f_obj())
print(f_obj())
print(f_obj())

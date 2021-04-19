# аргументы функций


# позиционные аргументы|параметры - обязательные
def first_func(var1, var2, var3):
    return var1 + var2 ** var3


print(first_func(10, 2, 3))


# именованные аргументы - обязательные
def second_func(var1, var3, var2):
    return var1 + var2 ** var3


print(second_func(var1=10, var2=2, var3=3))


# необязательные аргументы - var2, var3
def third_func(var1, var2=2, var3=3):
    return var1 + var2 ** var3


print(third_func(10))


def my_func(*args):
    return args


print(my_func(1, 2, 3, 4, 'str', True))


def my_func_1(**kwargs):
    return kwargs


print(my_func_1(var1=1, var2=2, var3=True, var4='str'))

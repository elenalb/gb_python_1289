import functools

# pip install functools - in terminal


# reduce()
def my_func(prev_el, el):
    # prev_el - предыдущий элемент
    # el - текущий элемент
    return prev_el + el


print(functools.reduce(my_func, [10, 20, 30, 40]))
# [10, 20, 30, 40]
# 10 + 20 = 30
# [30, 30, 40]
# 30 + 30 = 60
# [60, 40]
# 60 + 40 = 100


# partial()
def my_func_1(param1, param2):
    return param1 ** param2


# my_func_1(2, 3)
# new_my_func_1(param2):
#     param1 = 2
#     my_func_1(param1, param2)
new_my_func_1 = functools.partial(my_func_1, param2=2)
print(new_my_func_1)
print(new_my_func_1(4))

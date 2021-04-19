# анонимные функции

my_func = lambda arg1, arg2: arg1 + arg2

print(my_func(10, 20))
print((lambda arg1, arg2: arg1 + arg2)(2, 5))
print((lambda *args: args)(1, 2, 3, True))


def named_func(digit):
    return digit ** 2


print(named_func(2))


lambda_func = lambda digit: digit ** 2
print(lambda_func(2))

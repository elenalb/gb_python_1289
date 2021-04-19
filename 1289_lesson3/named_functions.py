# именные функции


def my_sum(arg1, arg2):
    # логика работы функции
    return arg1 + arg2


# print(my_sum(1, 2))
# print(my_sum('hello,', 'world!'))


def ext_func(arg1):
    def int_func(arg2, arg3, message):
        def print_message(message):
            print(message)
        print_message(message)
        return arg1 + arg2 + arg3
    return int_func


f_obj = ext_func(10)
print(f_obj)
print(f_obj(10, 20, "message!"))


def my_func():
    # написать логику позднее
    pass  # оператор-заглушка


print(my_func())

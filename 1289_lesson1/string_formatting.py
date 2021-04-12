# способы форматирования строк

# оператор %
# %s - string, %d - int, %f - float, %o - восьмеричная система, %x - шестнадцатеричная
world = "world"
my_string = "Hello, %s" % world
print(my_string)

print("%+10s %+10s %+10s" % ("param1", "param2", "param3"))

print("%.3f" % (20 / 8))

# метод format()
print("{}".format("arg1"))
print("{:>20} {:>20}".format("param1", "param2"))
print("{:.2f}".format(9 / 5))

# f-string
ip = '192.168.1.1'
mask = 10

print(f"ip-params: {ip}, mask: {mask}")

my_list = ['hello', 'world']
print(f"{', '.join(my_list)}")

a = 10
print(f"{a:>10} {a:<10}")

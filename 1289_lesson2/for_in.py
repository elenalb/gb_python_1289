# цикл for in

# for [переменная-итератор] in [последовательность]:
#     [действия, выполняемые для каждой переменной]

for element in [1, 2, 3]:
    print(element)

for el in (1, 2, 3, True):
    print(el)

for el in "my_string":
    print(el)

my_list = [1, 2, 3]
new_list = []
for el in my_list:
    new_list.append(el)
print(new_list)

my_dict = {1: 'one', 2: 'two'}
for key, value in my_dict.items():
    print(key, value)

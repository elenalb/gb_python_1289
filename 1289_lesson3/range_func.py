# функция range()
print(list(range(10)))
print(list(range(10, 20)))
print(list(range(10, 20, 2)))
print(list(range(10, 5)))

my_list = [1, 2, 3, 4]
for ind in range(len(my_list)):
    print(my_list[ind])


for el in range(1, 15, 2):
    res = el / 2
    print(f"Результат деления {el} на 2: {res}")

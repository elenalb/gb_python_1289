# строки
my_str = "hello, world!"
print(my_str)
print(type(my_str))

# конкатенация
s_1 = "hello, "
s_2 = "world!"
print(s_1 + s_2)

# взятие элемента по индексу
print(my_str[0])

# извлечение среза
# [s:f:step]
print(my_str[1:5])
print(my_str[:5])
print(my_str[4:])
print(my_str[:])
print(my_str[1:10:2])
print(my_str[::-1])
print(my_str[-2])

# механизмы реверса строк
# срез с отрицательным шагом
print(my_str[::-1])

# # обратная итерация
# for el in reversed(my_str):
#     print(el, end="")

# реверс на месте
reversed_str = ''
symbols = list(my_str)
for el in range(len(my_str) // 2):
    tmp = symbols[el]
    symbols[el] = symbols[len(my_str) - el - 1]
    symbols[len(my_str) - el - 1] = tmp
reversed_str = ''.join(symbols)
print(reversed_str)

# длина строки
print(len(my_str))
print(my_str.split())
print('; '.join(['a', 'b', 'c', 'd']))
print(my_str.title())
print(my_str.upper())  # str.lower()
print(my_str.istitle())
print(my_str.count('l'))
print(my_str.replace('l', 'o'))

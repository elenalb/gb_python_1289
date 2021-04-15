# списки
my_list = list('my string')
print(my_list)
new_list = [1, 2, True, "string", [1, 2]]
print(new_list)

# добавление элемента в список
new_list.append(False)
print(new_list)

# расширение списка
new_list.extend([10, 11, 12])
print(new_list)

new_list.insert(2, 3)
print(new_list)

new_list.remove(False)
print(new_list)

new_list.pop(0)
print(new_list)

print(new_list.index('string'))

print(new_list.count(10))

new_list.reverse()
print(new_list)

new_list_1 = new_list.copy()
print(new_list_1)

my_list = [1, 1, 1, 2]
print(my_list.count(1))

my_list.clear()
print(my_list)

# операторы in и is
# in - проверяет вхождение
my_list = [1, 2, 3, 4, 5]
print(4 in my_list)
print((4 and 10) in my_list)
print((4 or 10) in my_list)

# is - проверяет идентичность
list_1 = [1, 2, 3]
list_2 = [1, 2, 3]
print(list_1 is list_2)

list_2 = list_1
print(list_1)
print(list_2)
list_1.remove(2)
print(list_2)
print(list_1 is list_2)
print(id(list_1))
print(id(list_2))

list_2 = list_1.copy()
print(list_1 is list_2)

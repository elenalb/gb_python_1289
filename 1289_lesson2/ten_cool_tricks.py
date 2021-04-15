# объединение списков без цикла
my_list = [[1, 2, 3], [2, 3, 4], [3, 4, 5]]
print(sum(my_list, []))

# поиск уникальных элементов в списке
a = [1, 1, 1, 2, 3, 4, 4, 5, 5, 6]
print(list(set(a)))

# обмен значениями через кортежи
var_1, var_2, var_3 = 1, 2, 3
print(var_1, var_2)
var_1, var_2 = var_2, var_1
print(var_1, var_2)

# вывод несуществующего ключа в словаре
my_dict = {1: 'one', 2: 'two'}
print(my_dict.get(3))

# поиск самых частовстречающихся элементов списка
print(max(set(a), key=a.count))

# распаковка последовательностей при неизвестном количестве элементов
b = [1, 2, 3, 4]
el1, el2, el3, el4 = b
print(el1, el2, el3, el4)
*el1, el2, el3 = b
print(el1, el2, el3)
el1, *el2, el3 = b
print(el1, el2, el3)
el1, el2, *el3 = b
print(el1, el2, el3)
el1, el2, el3, el4, *el5 = b
print(el1, el2, el3, el4, el5)

# вывод с помощью функции print() без переноса строки
for el in "str":
    print(el, end='')

print("hello")

# сортировка словаря по значениям
my_dict = {'python': 1991, 'java': 1995, 'c++': 1983}
print(sorted(my_dict))  # сортировка по ключам
print(sorted(my_dict, key=my_dict.get))  # сортировка по значениям

# нумерованные списки
for ind, el in enumerate(['zero', 'one', 'two']):
    print(ind, el)

# транспонирование матрицы
# 1 2 3
# 2 3 4

# 1 2
# 2 3
# 3 4

matrix = [[1, 2, 3], [2, 3, 4]]
transp_matrix = zip(*matrix)
print(list(transp_matrix))

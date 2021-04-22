# генераторы списков и словарей

# генераторы списков - list comprehensions
my_list = [1, 2, 3]
new_list = [el * 2 for el in my_list]
print(f"Исходный список: {my_list}")
print(f"Новый список: {new_list}")

# аналог без генератора
# new_list_1 = []
# for el in my_list:
#     new_list_1.append(el * 2)
# print(f"Новый список: {new_list_1}")

lines = [line.strip() for line in open("txt")]
print(lines)

my_list_1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_list_1 = [el for el in my_list_1 if el % 2 == 0]
print(new_list_1)

str_1 = "abc"
str_2 = "de"
str_3 = "f"

sets = [i+j+k for i in str_1 for j in str_2 for k in str_3]
print(sets)


my_tuple = (2, 4, 6)
new_tuple = (el * 2 for el in my_tuple)
print(new_tuple)  # ПОЛУЧАЕМ ОБЪЕКТ!!! не кортеж

for element in new_tuple:
    print(element)


# генераторы словарей и множеств
my_dict = {el: el * 2 for el in my_list}
print(my_dict)

my_set = {el * 2 for el in my_list}
print(my_set)
print(type(my_set))

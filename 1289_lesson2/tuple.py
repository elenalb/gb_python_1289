# кортежи
# кортеж - неизменяемая структура!
my_tuple = tuple("my string")
new_tuple = (1, 2, 3, True, "string")
print(my_tuple)
print(new_tuple)

print(new_tuple.count(2))
print(new_tuple.index(True))

new_list = [1, 2, 3, True, "string"]
print(new_tuple.__sizeof__())
print(new_list.__sizeof__())

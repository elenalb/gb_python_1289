# оператор is - оператор идентичности

a = 20
b = 20

message = "Переменные идентичны" if a is b else "Переменные не идентичны"
print(message)

# == - оператор равенства значений
list_1 = [1, 2, 3]
list_2 = list_1

print(list_1 is list_2)
print(list_1 == list_2)

list_2 = list_1.copy()
print(list_1 is list_2)
print(list_1 == list_2)

a = "str"
print(a is None)

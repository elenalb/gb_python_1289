# множества
# изменяемые - set()
# неизменяемые - frozenset()

my_set = set("abrakadabra")
my_frozenset = frozenset("abrakadabra")
new_set = {1, 2, 3, 3, 3, 3, "string"}
print(my_set)
print(my_frozenset)
print(new_set)

my_set.add(1)

my_set.remove("a")
print(my_set)
my_set.discard("a")
print(my_set)

my_set.pop()  # удаляет ПЕРВЫЙ элемент множества
print(my_set)

my_set.clear()
print(my_set)

# модуль random

# генерация целых случайных чисел
from random import randint, randrange

print(randint(0, 20))
print(randint(-100, 20))

print(randrange(10))
print(randrange(10, 100))
print(randrange(10, 100, 5))

# генерация дробных случайных чисел
from random import random, uniform

print(random())
print(random() * 10)
print(random() * (10 - 4) + 4)

print(uniform(4, 10))


# другие функции
from random import choice, shuffle

print(choice([1, 2, True, 'text']))
my_list = [1, 2, True, 'text']
shuffle(my_list)
print(my_list)

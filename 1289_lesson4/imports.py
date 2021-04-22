# импортирование

# импорт из стандартной библиотеки
# 1 способ
import time
import random

print(time.time())
print(random.random())

# 2 способ
from time import time
from random import random

print(time())
print(random())

# импорт из собственного модуля
# 1 способ
import my_functions

my_functions.show_msg()
print(my_functions.simple_calc())

# 2 способ
from my_functions import show_msg, simple_calc

show_msg()
print(simple_calc())


import my_functions as mfunc

mfunc.show_msg()

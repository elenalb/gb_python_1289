"""
Узнайте у пользователя число n. Найдите сумму чисел n + nn + nnn.
Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.
"""

n = input('Введите целое число n: ')
num0 = int(n)
num1 = int(n + n)
num2 = int(n + n + n)
number = num0 + num1 + num2
print(f'Результат вычисления по формуле n+nn+nnn равен: {num0 + num1 + num2}')

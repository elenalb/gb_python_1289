# цикл while

number = int(input("Введите целое число от 0 до 9: "))

while number < 10:
    print(number)
    number += 1

print("Программа завершена")

# зацикливание
# a = 5
# while a > 0:
#     print("!", end='')

# инструкции break, continue
i = 0
while True:
    i += 1
    if i > 7:
        print("i > 7! Выходим из цикла")
        break
    if i % 2 != 0:
        print("i нечетное! Начинаем цикл заново")
        continue
    print("Число i равно ", i)

# ветвления

a = int(input("Введите число: "))
if a % 2 == 0:
    print("a is even")
else:
    print("a is odd")

a = int(input("Введите число: "))
if a % 2 == 0 and a > 10:
    if a > 10:
        print("a > 10!")
    else:
        print("a < 10!")
    print("a is even")
else:
    print("a is odd")

# ветвления на одном уровне вложенности

color = "blue"

if color == "green":
    print("зеленый")
elif color == "blue":
    print("синий")
elif color == "blue":
    print("синий")
else:
    print("Неизвестный цвет")

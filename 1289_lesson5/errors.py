# выявление ошибок при работе с файлами

# try:
#     f_obj = open("test")
#     for line in f_obj:
#         print(line)
# except FileNotFoundError:
#     print("Файл не найден!")
# finally:
#     f_obj.close()

try:
    with open("test") as f_obj:
        for line in f_obj:
            print(line)
except FileNotFoundError:
    print("Файл не найден!")


try:
    with open("text", "w") as file:
        file.write("Hello!")
except IOError:
    print("Ошибка ввода-вывода")


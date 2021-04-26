# режимы доступа к файлу

# r - read
# w - write, удаление всего содержимого, если файл есть. если нет - будет создан
# x - write, файл на запись, если его нет. Если есть - файл создан не будет
try:
    with open("text", "x") as file:
        for line in file:
            print(line)
except FileExistsError:
    print("Файл уже существует!")

with open("text1", "x") as file:
    file.write("new file")

# a - append, добавляет данные в конец файла
with open("text", "a") as file:
    file.write("\nWorld!")

# b - binary
# t - text
# + - read AND write

with open("text", "w+") as f_obj:
    f_obj.write("\nnew string\n")
    content = f_obj.read()
    print(content)

# параметры файлового объекта
# file.closed
# file.mode
# file.name

file = open("text")
print(file.closed)
print(file.mode)
print(file.name)
file.close()
print(file.closed)

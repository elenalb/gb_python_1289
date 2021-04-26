# определение позиции указателя в файле

with open("text", "w+") as f_obj:
    f_obj.write("new string\n")
    print(f_obj.tell())
    f_obj.seek(0)
    content = f_obj.read()
    print(content)

# file.tell() - определяет позицию указателя в файле
# file.seek() - перемещает указатель. 0 - в начало, 2 - в конец, 1 - текущая позиция
file = open("text")
print(file.tell())
content = file.read()
print(file.tell())
file.seek(0)
print(content)
content_new = file.read()
print(content_new)
file.close()

# чтение данных из файла

f = open("text", "r")

# f_obj = open(r"C:\Users\elena.babenko\PycharmProjects\1289_gb_python\1289_lesson5\text")
# # \t, \n, \s, \p

# # read() -- считывает файл полностью
content = f.read()
print(content)
# файл необходимо ВСЕГДА закрывать
# f.close()

# # readline() -- позволяет извлечь очередную строку
content = f.readline()
print(content)
content1 = f.readline()
print(content1)
print(f.readline())
# f.close()

# # readlines() -- список из всех строк файла
content = f.readlines()
print(content)
# f.close()

# считывание файла по частям
while True:
    content = f.read(7)
    print(content)

    if not content:
        break

for line in f:
    print(line)

f.close()

# # считывание бинарных файлов
file = open("text", "rb")  # read-binary
for line in file:
    print(line)
file.close()

# # запись данных в файл
out_f = open("file_to_write", "w")
# out_f.write("hello, world!\nsecond string")
# out_f.close()

out_f.writelines(["hello!\n", "world!\n", "third string"])
out_f.close()

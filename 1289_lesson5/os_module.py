import os

# # удаление файла
# os.remove("text1")

# переименование файла
# os.rename("text", "test")

# список файлов и папок в директории
content = os.listdir(path="..")
print(content)

# подмодуль path
print(os.path.basename(r"C:\Users\elena.babenko\PycharmProjects\1289_gb_python\1289_lesson5\test"))
print(os.path.dirname(r"C:\Users\elena.babenko\PycharmProjects\1289_gb_python\1289_lesson5"))
print(os.path.exists(r"C:\Users\elena.babenko\PycharmProjects\1289_gb_python\1289_lesson5\text"))
print(os.path.isdir(r"C:\Users\elena.babenko\PycharmProjects\1289_gb_python\1289_lesson5\text"))
print(os.path.isfile(r"C:\Users\elena.babenko\PycharmProjects\1289_gb_python\1289_lesson5\test"))

path = os.path.join("bin", "new_dir")
print(path)
print(os.path.split(path))
# bin/new_dir

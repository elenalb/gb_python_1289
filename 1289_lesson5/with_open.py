# менеджеры контекста

# f = open("text", "r")
# for line in f:
#     print(line)
# f.close()

# аналог

with open("text", "r") as f:
    for line in f:
        print(line)

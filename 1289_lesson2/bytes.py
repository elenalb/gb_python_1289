# байты
print(b'text')
print('текст'.encode('utf-8'))
print(bytes('текст', encoding='utf-8'))
print(bytes([1, 2, 3]))

# bytearray
my_var = bytearray(b"some text")
print(my_var)
print(my_var[0])

# словари
my_dict = dict(key_1='value_1', key_2='value_1')
print(my_dict)

new_dict = {1: 'one', 2: 'two'}
print(new_dict)

print(new_dict.keys())
print(new_dict.values())
print(new_dict.items())
print(new_dict[1])
print(new_dict.get(1))
print(new_dict.get(4))
# print(new_dict.popitem())
# print(new_dict)
print(new_dict.pop(2))
print(new_dict)
new_dict.update({2: 'two', 3: 'three'})
print(new_dict)
new_dict.clear()
print(new_dict)

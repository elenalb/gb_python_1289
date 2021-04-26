# JSON
import json

# сериализация - преобразование к json-формату
# dump(), dumps()
# dict -> object
# list, tuple -> array
# str -> string
# int, float -> number
# True -> true
# False -> false
# None -> null

data = {
    "income": {
        "salary": 50000000,
         "bonus": 200000
    }
}

# with open("dict_to_json.json", "w") as file:
#     json.dump(data, file)

json_str = json.dumps(data)
print(json_str)
print(type(json_str))

# десериализация
# load(), loads()

with open("dict_to_json.json") as file:
    data_new = json.load(file)

print(data_new)
print(type(data_new))

new_dict = json.loads(json_str)
print(new_dict)
print(type(new_dict))

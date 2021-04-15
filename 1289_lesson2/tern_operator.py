# тернарный оператор

# condition_if_true if condition else condition_if_false
is_checked = False
mode = "checked" if is_checked else "not checked"
print(mode)

# (condition_if_false, condition_if_true)[condition]
is_checked = True
mode = ("not checked", "checked")[is_checked]
print(mode)

print(True or "Some")
print(False or "Some")

func_return = "func_return"
message = func_return or "Функция ничего не вернула"
print(message)

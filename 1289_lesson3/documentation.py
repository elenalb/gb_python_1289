# документирование функций
# PEP-257
my_path = None


def get_path():
    """Возвращает путь до директории"""
    global my_path
    if my_path:
        return my_path


def my_func(arg1=0, arg2=1):
    """
    Возвращает результат деления arg1 на arg2

    :param arg1: int, default = 0
    :param arg2: int, default = 1
    :return: результат деления arg1 на arg2
    """
    return arg1 / arg2

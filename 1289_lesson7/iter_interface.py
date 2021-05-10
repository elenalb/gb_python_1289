# интерфейс итерации

my_list = [1, 2, 3]
for el in my_list:
    print(el)

# __iter__() для my_list
# my_list.__iter__()
# for in -> __next__() -> StopIteration or next element


class Iterator:
    """
    Объект-итератор
    """
    def __init__(self, start=0):
        self.i = start

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


class IterObj:
    """
    Объект, который поддерживает интерфейс итерации
    """
    def __init__(self, start=0):
        self.start = start - 1

    def __iter__(self):
        return Iterator(self.start)


obj = IterObj(start=2)
for el in obj:
    print(el)
for el in obj:
    print(el)


class Iter:
    def __init__(self, start=0):
        self.i = start - 1

    def __iter__(self):
        return self

    def __next__(self):
        self.i += 1
        if self.i <= 5:
            return self.i
        else:
            raise StopIteration


obj1 = Iter()
for el in obj1:
    print(el)

for el in obj1:
    print(el)

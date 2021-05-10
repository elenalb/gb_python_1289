# композиция

# вычисление площади обоев
# len1 * height, len2 * heigh
# S = 2 * (len1 * height + len2 * height)
# вычитаем площади окон и дверей


class WindowDoor:
    def __init__(self, wd_len, wd_height):
        self.square = wd_len * wd_height


class Room:
    def __init__(self, len1, len2, height):
        self.square = 2 * height * (len1 + len2)
        self.wd = []

    def add_win_door(self, wd_len, wd_height):
        self.wd.append(WindowDoor(wd_len, wd_height))

    def common_square(self):
        main_square = self.square
        for el in self.wd:
            main_square -= el.square
        return main_square


r = Room(10, 20, 4)
print(r.square)
r.add_win_door(2, 2)  # add window
r.add_win_door(2, 2)  # add window
r.add_win_door(2, 3)  # add door
print(r.wd)
print(r.common_square())

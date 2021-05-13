# встроенные атрибуты и методы объектов классов


class User:
    """
    class User
    """
    def __init__(self, name, login, password, email):
        self.name = name
        self.login = login
        self.password = password
        self.email = email

    def get_user_data(self):
        print(f"Имя: {self.name}, логин: {self.login}, "
              f"пароль: {self.password}, e-mail: {self.email}")


u = User("Ivan", "Iv", "11111", "ivan@gmail.com")
u.get_user_data()
u1 = User("sda", "sadsad", "dfsdf", "dsfdf")
u1.get_user_data()

print(f"__name__: {User.__name__}\n__module__: {User.__module__}"
      f"\n__dict__: {User.__dict__}\n__doc__: {User.__doc__}\n"
      f"__init__: {User.__init__}")

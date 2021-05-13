# пример ООП-программы
# 1. Сформулировать задачу
# 2. Определить объекты предметной области
# 3. Выделить классы, на основе которых генерируются объекты
# 4. Установить основные атрибуты и методы
# 5. Создать классы, атрибуты и методы
# 6. Создать объекты классов
# 7. Выполнить итоговое решение задачи

# Разработка виртуальной модели образовательного процесса
# Студенты, преподаватель, знания
# class Teacher, class Student, class Data
# class Person -> class Teacher, class Student
# class Person: name, surname
# class Teacher: to_teach()
# class Student: to_take(), knowledge_list
# class Subject: my_list()


class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def __str__(self):
        return f"Name and surname: {self.name} {self.surname}"


class Teacher(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        # Person.__init__(self, name, surname)

    def to_teach(self, subj, *students):
        for student in students:
            student.to_take(subj)


class Student(Person):
    def __init__(self, name, surname):
        super().__init__(name, surname)
        self.knowledge_list = []

    def to_take(self, subj):
        self.knowledge_list.append(subj)


class Subject:
    def __init__(self, *subjects):
        self.subjects = subjects

    def my_list(self):
        return self.subjects


s = Subject("maths", "physics")
t = Teacher("Elena", "B")
print(t)

s_1 = Student("Ivan", "Ivanov")
s_2 = Student("Alexey", "Ivanov")
s_3 = Student("Vladimir", "Ivanov")
print(s_1)
print(s_2)
print(s_3)

t.to_teach(s, s_1, s_2, s_3)
print(s_1.knowledge_list[0].my_list())
print(s_1.knowledge_list)

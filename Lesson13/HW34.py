# ДЗ 33. Группа студентов
# 1) Создайте класс, описывающий человека (создайте метод, выводящий информацию о человеке).
#
# 2) На его основе создайте класс Студент (переопределите метод вывода информации).
#
# 3) Создайте класс Группа, экземпляр которого, состоит из объектов класса Студент. Реализуйте методы добавления, удаления студента и метод поиска студента по фамилии.
#
# Метод поиска студента должен возвращать именно экземпляр класса Студент, если студент есть в группе, в противном случае - None.
#
# Определите для Группы метод str() для возвращения списка студентов в виде строки.
#
#
#
# Ниже представленны заготовки, которые необходимо дополнить.
from typing import Set, Any


class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.gender = gender

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = record_book

    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        self.group.add(student)

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)

    def find_student(self, last_name):
        for i in self.group:
            if last_name in str(i):
                return i
        return None

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += f'{str(i)}\n'
        return f'Group: {self.number}\n{all_students}'


st1 = Student('Male', 30, 'Steve', 'Jobs', 'AN142')
st2 = Student('Female', 25, 'Liza', 'Taylor', 'AN145')
gr = Group('PD1')
gr.add_student(st1)
gr.add_student(st2)
print(gr)
print("Find student with last name - Jobs: ")
a = gr.find_student('Jobs')
print(a)
print("Find student with last name - Jobs2: ")
b = gr.find_student('Jobs2')  # None
print(b)
print("Delete student with last name - Taylor")
gr.delete_student('Taylor')
print(gr) # Only one student

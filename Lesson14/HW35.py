# ДЗ 35. Пользовательское исключение
# Модифицируйте класс Группа (задание прошлой лекции) так,
# чтобы при попытке добавления в группу более 10-ти студентов, было возбужденно
# пользовательское исключение. Таким образом нужно создать еще и пользовательское исключение для этой ситуации. И обработать его.

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
        if len(self.group) >= 10:
            raise ValueError('В группе уже 10 человек. Больше добавить нельзя')
        else:
            self.group.add(student)
            return 'Пользователь добавлен'

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
st3 = Student('Female', 25, 'Masha', 'Taylor', 'AN145')
st4 = Student('Female', 25, 'Dasha', 'Taylor', 'AN145')
st5 = Student('Female', 25, 'Nastya', 'Taylor', 'AN145')
st6 = Student('Female', 25, 'Sveta', 'Taylor', 'AN145')
st7 = Student('Female', 25, 'Lena', 'Taylor', 'AN145')
st8 = Student('Female', 25, 'Polina', 'Taylor', 'AN145')
st9 = Student('Female', 25, 'Vita', 'Taylor', 'AN145')
st10 = Student('Female', 25, 'Natasha', 'Taylor', 'AN145')
st11 = Student('Female', 25, 'Erika', 'Taylor', 'AN145')
gr = Group('PD1')
a = gr.add_student(st1)
print(a)
b = gr.add_student(st2)
print(b)
c = gr.add_student(st3)
print(c)
d = gr.add_student(st4)
print(d)
e = gr.add_student(st5)
print(e)
f = gr.add_student(st6)
print(f)
g = gr.add_student(st7)
print(g)
h = gr.add_student(st8)
print(h)
i = gr.add_student(st9)
print(i)
j = gr.add_student(st10)
print(j)
try:
    gr.add_student(st11)
except ValueError as e:
    print(e)

print(gr)
print("Find student with last name - Jobs: ")
a = gr.find_student('Jobs')
print(a)
print("Find student with last name - Jobs2: ")
b = gr.find_student('Jobs2')  # None
print(b)
print("Delete student with last name - Taylor")
gr.delete_student('Taylor')
print(gr)
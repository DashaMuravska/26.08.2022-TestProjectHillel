class Human:

    def __init__(self, gender, age, first_name, last_name):
        self.first_name = input("Имя: ")
        self.last_name = input("Фамилия: ")
        self.age = input("Возраст: ")
        self.gender = input("Пол: ")

    def __str__(self):
        return f'{self.first_name} {self.last_name}, {self.age} years, {self.gender}'


class Student(Human):

    def __init__(self, gender, age, first_name, last_name, record_book):
        super().__init__(gender, age, first_name, last_name)
        self.record_book = input("Номер: ")

    def __str__(self):
        return f'{super().__str__()}, {self.record_book}'


class Group:

    def __init__(self, number):
        self.number = number
        self.group = set()

    def add_student(self, student):
        if len(self.group) <= 2:
            self.group.add(student)
            return 'Пользователь добавлен'
        else:
            raise ValueError('В группе уже 2 человекa. Больше добавить нельзя')

    def delete_student(self, last_name):
        res = self.find_student(last_name)
        self.group.discard(res)
        return 'Студент удален'

    def find_student(self, last_name):
        last_name = input('Ввести фамилию: ')
        for i in self.group:
            if last_name in str(i):
                return i
        return None

    def __str__(self):
        all_students = ''
        for i in self.group:
            all_students += f'{str(i)}\n'
        return f'Group: {self.number}\n{all_students}'


gr = Group('PD1')

while True:
    print("1. Добавить студента")
    print("2. Найти студента")
    print("3. Удалить студента")
    print("4. Показать группу")
    print("0. Закончить работу")
    cmd = input("Выберите пункт: ")

    if cmd == "1":
        str1 = Student(1, 1, 1, 1, 1)
        try:
            a = gr.add_student(str1)
            print(a)
        except ValueError as e:
            print(e)
    elif cmd == "2":
        a = gr.find_student(1)
        print(a)
    elif cmd == "3":
        b = gr.delete_student(1)
        print(b)
    elif cmd == "4":
        print(gr)
    elif cmd == "0":
        break
    else:
        print("Вы ввели не правильное значение")


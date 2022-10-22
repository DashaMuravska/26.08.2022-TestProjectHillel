# Создайте класс «Прямоугольник», у которого необходимо реализовать два поля (ширина и высота) и несколько обязательных методов:

# Метод сравнения прямоугольников по площади.
# Метод сложения прямоугольников (площадь суммарного прямоугольника должна быть равна сумме площадей прямоугольников, которые вы складываете).
# Методы умножения прямоугольника на число n (это должно увеличить площадь базового прямоугольника в n раз).
# В классе могут быть созданы и дополнительные (вспомогательные методы)
#
# Несколько уточнений:
#
# 1. Методы сложения, умножения, деления и т.д. обязательно должны возвращать новый экземпляр класса Прямоугольник!
#
# 2. Для умножения, сложения, сравнения, обязательно нужно переопределять "магичиские" методы. Для умножение есть встроенный метод mul
#
# 3. Когда в результате мат. действий создаете новый экземпляр класса Прямоугольник, то у этого экземпляра, перемножение сторон, должно
# давать нужную площадь. Это тоже важно

class Rectangle:

    def __init__(self, width, height):
        self.width = width
        self.height = height

    def get_square(self):
        return self.width * self.height

    def __eq__(self, other):
        if self.get_square() == other.get_square():
            return True
        return False

    def __add__(self, other):
        return Rectangle(self.get_square() + other.get_square(), 1)

    def __mul__(self, n):
        return Rectangle(self.get_square() * n, 1)

    def __truediv__(self, other):
        return Rectangle(self.get_square() / other.get_square(), 1)

    def __str__(self):
        return f'Rectangle [width = {self.width}, height = {self.height}'


r1 = Rectangle(2, 4)
r2 = Rectangle(3, 6)
print(r1.get_square())  # 8
print(r2.get_square())  # 18

r3 = r1 + r2
print(r3.get_square())  # 26

r4 = r1 * 4
print(r4.get_square())  # 32

r5 = r1 / r2
print(r5.get_square())

print(r1 == r2)
# Создайте класс «Правильная дробь» и реализуйте методы сравнения, сложения, вычитания и произведения для экземпляров этого класса.

class Fraction:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    def __mul__(self, other):
        new_a = self.a * other.a
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __add__(self, other):
        new_a = (self.a * other.b) + (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __sub__(self, other):
        new_a = (self.a * other.b) - (other.a * self.b)
        new_b = self.b * other.b
        return Fraction(new_a, new_b)

    def __eq__(self, other):
        x = self.a / self.b
        y = other.a / other.b
        if x == y:
            return True
        else:
            return False

    def __gt__(self, other):
        x = self.a / self.b
        y = other.a / other.b
        if x > y:
            return True
        else:
            return False

    def __lt__(self, other):
        x = self.a / self.b
        y = other.a / other.b
        if x < y:
            return True
        else:
            return False

    def __str__(self):
        return f"Fraction: {self.a}/{self.b}"


f_a = Fraction(2, 3)
f_b = Fraction(3, 6)
f_c = f_b + f_a
print(f_c)  # Fraction: 21, 18
f_d = f_b * f_a
print(f_d)  # Fraction: 6, 18
f_e = f_a - f_b
print(f_e)  # Fraction: 3, 18

print(f_d < f_c)  # True
print(f_d > f_e)  # True
print(f_a == f_b)  # False
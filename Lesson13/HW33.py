# ДЗ 34. Класс "Цифровой счетчик"
# Создать класс цифрового счетчика. В классе реализовать методы:
#
# установка максимального значения счетчика,
# установка минимального значения счетчика
# установка начального значения счётчика
# метод увеличения счетчика на 1. Метод можно вызывать до тех пор, пока значение не достигнет максимума. Потом - выкинуть (raise) исключение ValueError, с описанием, что достигнут максимум
# уменьшения счетчика на 1. Метод можно вызывать до тех пор, пока значение не достигнет минимума. Потом - выкинуть (raise) исключение ValueError, с описанием, что достигнут минимум
# возвращения текущего значения счётчика
# Начальное, минимальное и максимальное значения счетчика, также могут быть добавлены в метод инициализации экземпляра класса.
#
#
#
# Приблизительный каркас для класса и варианты проверки. Вам нужно дописать необходимое вместо pass

class Counter:

    def __init__(self, current=7, min_value=0, max_value=10):
        self.current = current
        self.min_value = min_value
        self.max_value = max_value

    def set_current(self, start):
        self.current = start

    def set_max(self, max_max):
        self.max_value = max_max

    def set_min(self, min_min):
        self.min_value = min_min

    def step_up(self):
        if self.current >= self.max_value:
            raise ValueError("Достигнут максимум")
        else:
            self.current += 1
            return self.current

    def step_down(self):
        if self.current <= self.min_value:
            raise ValueError("Достигнут минимум")
        else:
            self.current -= 1
            return self.current

    def get_current(self):
        return self.current


counter = Counter()
counter.set_current(7)
counter.set_max(10)
print("Текущее значение", counter.get_current())
a = counter.step_up()
print(a)
b = counter.step_up()
print(b)
c = counter.step_up()
print(c)
try:
    counter.step_up()  # ValueError
except ValueError as e:
    print(e)  # Достигнут максимум
print("Текущее значение ", counter.get_current())  # 10
counter.set_min(7)
d = counter.step_down()
print(d)
e = counter.step_down()
print(e)
f = counter.step_down()
print(f)

try:
    counter.step_down()  # ValueError
except ValueError as e:
    print(e)  # Достигнут минимум


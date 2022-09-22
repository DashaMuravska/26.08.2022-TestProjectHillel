# ДЗ 16. Приветствие
#
# Написать функцию say_hi, которая представит человека по переданным параметрам.
#
# Входные данные: Два аргумента строка(str) и положительное число(int)
#
# Функция должна вернуть строку.
#
#
#
# say_hi("Alex", 32) == "Hi. My name is Alex and I'm 32 years old"
# say_hi("Frank", 68) == "Hi. My name is Frank and I'm 68 years old"
name = (input("Enter your name: "))
age = (input("Enter your age: "))


def say_hi(a, b):
    hi = f"Hi. My name is {name} and I'm {age} years old"
    return hi


print(say_hi(name, age))

# Пользователь вводит через дефис две буквы, Ваша задача написать программу, которая будет возвращать все символы между ними включительно.
# Никаких проверок на ошибку делать не надо, минимальное значение всегда меньше или равно максимальному.
# Подсказка: Используйте модуль string , в котором есть string.ascii_letters, со всем набором необходимых букв
# Пример:

# "a-c" -> abc
# "a-a" -> a
# "s-H" -> stuvwxyzABCDEFGH
# "a-A" -> abcdefghijklmnopqrstuvwxyzA

# import string
#
# string1 = 's-H'
# str_len = len(string1)
# string2 = ''
# for i in range(str_len):
#     string2 = string.ascii_letters[i]
#     print(string2)

# import string
#
# string1 = 'a-c'
# lst = list()
# a = string.ascii_letters[0]
# b = string.ascii_letters[-1]
# lst = [a, b]
# print(lst)

from string import ascii_letters

string1 = 'a-c'
# string1 = 'a-a'
# string1 = 'a-A'
# string1 = 'a-A'
print(string1)
a = string1[0]
b = string1[-1]
print(ascii_letters[ascii_letters.index(a):ascii_letters.index(b) + 1])





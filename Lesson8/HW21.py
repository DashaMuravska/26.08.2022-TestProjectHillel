# Ваша задача — написать функцию is_palindrome, которая будет проверять, является ли предложение палиндромом.
#
# Палиндромом — это некоторое предложение, которое читается одинаков слева на право и справа налево без учета знаков пунктуации.
#
# Функция принимает на вход строку, а возвращает булевое значение True\False
#
#
#
# Пример:
#
#
#
# is_palindrome('A man, a plan, a canal: Panama') -> True
# is_palindrome('0P') -> False
# is_palindrome('a.') -> True
import string


def is_palindrome(some_string):
    some_string = some_string.lower()
    ss = some_string
    some_string_len = len(some_string)
    for i in range(some_string_len):
        if some_string[i] in string.punctuation or some_string[i] in ' ':
            ss = ss.replace(some_string[i], '')
    revers = ss[::-1]
    if ss == revers:
        c = True
    else:
        c = False

    return c


str1 = input("Введите строку: ")
print(is_palindrome(str1))







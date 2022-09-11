# Пользователь вводит строку. Ваша задача - проверить, может ли эта строка, быть именем переменной.
#
# Переменная не может начинаться с цифры, состоять только из цифр, не может содержать заглавные буквы и знаки пунктуации, кроме нижнего подчеркивания "_" . Также, она не может быть ни одним из зарегистрированных слов. При этом имя переменной, может состоять только из одного нижнего подчеркивания "_" .
#
# Зарегистрированные слова можно взять из keyword.kwlist.
#
# В итоге проверки, на печать выводится True, если такое имя переменной допустимо, и False - в противном случае.
#
# Примеры имен переменных и результат (=> на печать выводить не нужно :))
#
# _ => True
#
# x => True
#
# get_value => True
#
# Get_value => False
#
# get_Value => False
#
# getValue => False
#
# 3m => Fals

import string
import keyword

s = input("Enter some name: ")
a = len(s)
if s[0].isdigit():
    print("False")
elif s.isdigit():
    print("False")
elif keyword.iskeyword(s):
    print("False")
elif s.count("_") > 1:
    print("False")
for i in range(a):
    if s[i] in string.ascii_uppercase:
        print("False")
    elif s[i] in string.punctuation and '_' not in s[i]:
        print("False")
else:
    print("True")

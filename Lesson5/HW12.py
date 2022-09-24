# ДЗ 12. hashtag
#
# Пользователь вводит строку, Ваша задача — преобразовать строку в hashtag.
#
# Парочка правил:
#
# никаких символов из набора string.punctuation быть не должно, в том числе и пробелов;
# итоговая длина hashtag должна быть не более 140 символов.
# Каждое слово начинается с заглавной буквы.
# Если длина хэштега более 140 символов - обрезать итоговую строку до 140 символов.
import string
a = input("Enter some string: ")
a_len = len(a)
a = a.title()
b = a
for i in range(a_len):
    if a[i] in string.punctuation or a[i]:
        b = b.replace(a[i], '')
lst = b.split()
s = "".join(lst)
s = s[:140]
print("#" + s)

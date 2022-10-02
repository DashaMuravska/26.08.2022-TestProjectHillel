# DZ 26 Найти первое слово
#
# Напишите функцию first_word, которая в переданной строке найдет ее первое слово.
#
# При решении задачи обратите внимание на следующие моменты:
#
#
#
# В строке могут встречаются точки и запятые
# Строка может начинаться с буквы или, к примеру, с пробела или точки
# В слове может быть апостроф и он является частью слова
# Весь текст может быть представлен только одним словом и все
#
#
#
# Входные параметры: Строка.
#
# Выходные параметры: Строка.
#
# Пример:
#
# first_word("Hello world") == "Hello"
#
# first_word("greetings, friends") == "greetings"
#
# first_word("don't touch it") == "don't"
#
# first_word("... and so on ...") == "and"
#
# first_word("hi") == "hi"
#
# first_word("Hello.World") == "Hello"

# def first_word(s):
#     spl = s.split()
#     first = spl[0]
#     return first
#
#
# first_word("Hello world")

def first_word(s):
    ex = [" ", "\'"]
    for i in s:
        if not i.isalpha() and i not in ex:
            s = s.replace(i, ' ')
    spl = s.split()
    f = spl[0]
    return f


b = first_word("Hello.World")
print(b)


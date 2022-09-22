# ДЗ 17. Модифицировать строку
#
# На вход функции correct_sentence передается одно предложение. Необходимо вернуть его исправленную копию так, чтобы оно всегда начиналось с большой буквы и заканчивалось точкой.
#
# Обратите внимание на то, что не все исправления необходимы. Если предложение уже заканчивается на точку, то добавлять еще одну не нужно, это будет ошибкой
#
# Входные аргументы: Строка (string).
#
# Выходные аргументы: Строка (string).
#
# Пример:
#
# correct_sentence("greetings, friends") == "Greetings, friends."
# correct_sentence("hello") == "Hello."
# correct_sentence("Greetings, friends") == "Greetings, friends."
# correct_sentence("Greetings, friends.") == "Greetings, friends."
# correct_sentence("greetings, friends.") == "Greetings, friends."

a = input("Enter some string: ")


def correct_sentence(some_string):
    if "." in some_string:
        some_string = some_string[0].upper() + some_string[1:]
    else:
        some_string = some_string[0].upper() + some_string[1:] + "."
    return some_string


print(correct_sentence(a))

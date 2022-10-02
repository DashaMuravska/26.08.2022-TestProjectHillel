# ДЗ 27. Проверить является ли число четным или нет
#
# Ваша функция is_even, должна возвращать True если число четное, и False если число нечетное.
#
#
# Входные данные: Целое число.
#
# Выходные данные: Логический тип.
#
# Пример:
#
# is_even(2) == True
#
# is_even(5) == False
#
# is_even(0) == True

def is_even(a):
    if a % 2 == 0:
        return True
    else:
        return False


b = is_even(0)
print(b)



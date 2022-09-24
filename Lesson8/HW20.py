# Ваша задача — написать функцию add_one,
# которая принимает список из цифр, которые являются одним числом, к которому необходимо добавить к числу 1.
# Т.е. Вам необходимо из набора цифр, входящего списка, получить число, сложить его с 1, и полученную сумму, снова разбить на список из цифр.
#
# В результате функция возвращает список из цифр, составляющих значение суммы.
#
#
#
# Примеры:
#
# add_one([1, 2, 3, 4]) возвращает [1, 2, 3, 5]
# add_one([9, 9, 9, 9]) возвращает [1, 0, 0, 0, 0]
# add_one([0]) возвращает [1]
# add_one([9]) возвращает [1, 0]

def add_one(lstnum):
    for i in range(len(lstnum)):
        lstnum[i] = str(lstnum[i])
    num = "".join(lstnum)
    required_num = int(num) + 1
    required_num = str(required_num)
    rlst =[]
    for i in range(len(required_num)):
        rlst.append(required_num[i])
    for i in range(len(rlst)):
        rlst[i] = int(rlst[i])
    return rlst


lstone = [1, 2, 3, 4]
print(add_one(lstone))




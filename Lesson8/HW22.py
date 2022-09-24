# Вам необходимо написать функцию find_unique_value, которая будет принимать список из чисела, находить среди них уникальное число и возвращать его.
#
#
#
# Пример:
#
# find_unique_value([1, 2, 1, 1]) -> 2
# find_unique_value([2, 3, 3, 3]) -> 2
# find_unique_value([5, 5, 5, 0.5]) -> 0.5

def find_unique_value(l):
    for i in range(len(l)):
        if l.count(l[i]) == 1:
            b = l[i]
    return b


a = [5, 5, 5, 0.5]
print(find_unique_value(a))

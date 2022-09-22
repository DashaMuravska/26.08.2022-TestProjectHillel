# ДЗ 19. Поиск совпадений
#
# Напишите программу, которая сгенерирует два списка с разным количеством элементов (кол-во формируется рандомно).
#
# Один список с числами кратными 3, другой с числами кратными 5.
#
# С помощью множеств создайте набор с числами, которые есть в обоих множествах (пересечение)

import random
first_list = []
second_list = []

a = random.randint(5, 20)
j = 3
k = 5

for i in range(a):
    first_list.append(j)
    j += 3
for i in range(a):
    second_list.append(k)
    k += 5

set1 = set(first_list)
set2 = set(second_list)
set3 = set1.intersection(set2)

print(first_list)
print(second_list)
print(set3)

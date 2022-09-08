# Найти сумму элементов с четными индексами
test_list = [1, 2, 3, 4, 5]
print(test_list)
l = len(test_list)
s = 0
if l != 0:
    for i in range(l):
        if i % 2 == 0:
            s += test_list[i]
    print("Sum = ", s * test_list[-1])
else:
    print(0)

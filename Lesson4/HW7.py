# Переместить все нули в конец списка
# test_list = [0, 1, 0, 3, 12]
test_list = [0]
# test_list = [1, 0, 3, 0, 0, 0, 5]
# test_list = [9, 0, 7, 31, 0, 45, 0, 45, 0, 0, 96, 0]
# len_list = len(test_list)
# j = 0
# for i in range(len_list):
#    if test_list[i] != 0:
#        test_list[i], test_list[j] = test_list[j], test_list[i]
#        j += 1
print(test_list)
lst3 = []
lst4 = []
a = len(test_list)
for i in range(a):
    if test_list[i] != 0:
        lst3.append(test_list[i])
    elif test_list[i] == 0:
        lst4.append(test_list[i])
print(lst3 + lst4)




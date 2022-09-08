test_list = [1, 2, 3, 4]
length = len(test_list)
if length % 2 == 0:
    mid = length // 2
    new_test_list = list()
    new_test_list.append(test_list[:mid])
    new_test_list.append(test_list[mid:])
    print(new_test_list)
else:
    mid = length // 2
    new_test_list = list()
    new_test_list.append(test_list[:mid + 1])
    new_test_list.append(test_list[mid + 1:])
    print(new_test_list)



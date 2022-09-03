test_list = [1, 2, 3]
length = len(test_list)
if length == 0:
    print(test_list)
else:
    old_index = test_list.index(length)
    test_list.insert(0, test_list.pop(old_index))
    print(test_list)

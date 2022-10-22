def remove_empty(file1):
    for i in range(len(file1)):
        file1[i] = file1[i].strip()
    lst = []
    for i in range(len(file1)):
        if file1[i] != '':
            lst.append(file1[i])
    txt = '\n'.join(lst)
    print(txt)


new_text = open('/home/daria/Downloads/cleaned.txt', 'r')
nt = new_text.readlines()
print(nt)
remove_empty(nt)
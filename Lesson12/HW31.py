# Ваша задача написать функцию, которая прочитает заданный файл, очистит текст от html-тэгов, и запишет этот текст в другой файл.
#
# html-тэг всегда начинается с "<" и заканчивается на ">" Т.е. нужно удалить эти символы и все, что между ними.
#
# Функция получает на вход два параметра - имя файла, который нужно очистить, и имя файла, куда нужно записать очищенный текст.
# Имя файла, куда нужно писать, можно задать значением по умолчанию.
#
# Пример файлов во вложении - файл который нужно очистить (расширение html) и файл, с очищенным текстом.
#
# Доп. задача для тех, кто захочет усложнить решение - попробуйте убрать строки, в которых нет информации.

# def remove_tags(html_file, result=open('/Users/jan/Desktop/cleaned_text.txt', 'w', encoding='utf-8')):
#     html_file = html_file.replace(html_file[html_file.find('<'):html_file.find('>') + 1], "")
#     if '<' and '>' in html_file:
#         remove_tags(html_file)
#     else:
#         result.write(html_file)
#         result.close()
#     return None
#
#
# raw_text = open('/Users/jan/Desktop/draft.html', 'r')
# ht = raw_text.read()
# remove_tags(ht)

def remove_tags(html_file, txt_file):
    html_file = html_file.replace(html_file[html_file.find('<'):html_file.find('>') + 1], "")
    if '<' and '>' in html_file:
        remove_tags(html_file, txt_file)
    else:
        txt_file.write(html_file)
        txt_file.close()


def remove_empty(file1, file2):
    for i in range(len(file1)):
        file1[i] = file1[i].strip()
    for i in range(len(file1)):
        file1[i] = file1[i].strip()
    lst = []
    for i in range(len(file1)):
        if file1[i] != '':
            lst.append(file1[i])
    txt = '\n'.join(lst)
    file2.write(txt)
    file2.close()


text = open('/home/daria/Downloads/draft.html', 'r')
new_text = open('/home/daria/Downloads/cleaned.txt', 'w')
ht = text.read()
remove_tags(ht, new_text)
new_text = open('/home/daria/Downloads/cleaned.txt', 'r')
new_text2 = open('/home/daria/Downloads/cleaned_new.txt', 'w')
nt = new_text.readlines()
remove_empty(nt, new_text2)






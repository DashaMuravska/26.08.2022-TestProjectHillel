# ДЗ 23. Определить популярность определенных слов в тексте
#
# На вход функции popular_words передаются 2 аргумента. Текст и массив слов, популярность которых необходимо определить.
#
# При решении этой задачи обратите внимание на следующие моменты
#
# Слова необходимо искать во всеx регистрах.
# Т.е. если необходимо найти слово "one", значит для него будут подходить слова "one", "One", "oNe", "ONE" и.т.д.
# Искомые слова всегда указаны в нижнем регистре
# Если слово не найдено ни разу, то его необходимо вернуть в словаре со значением 0 (ноль)
# Входные параметры: Текст и массив искомых слов.
#
# Выходные параметры: Словарь, в котором ключами являются искомые слова и значениями то, сколько раз они встречаются в исходном тексте.
#
# Пример:
#
# popular_words('''When I was One I had just begun When I was Two I was nearly new ''', ['i', 'was', 'three', 'near']) == { 'i': 4, 'was': 3, 'three': 0, 'near': 0 }
#
# Предусловия:
#
# Исходный текст будет состоять из букв английского алфавита в верхнем и нижнем регистре, а также пробелов.

def popular_words(text, word):
    d = {}
    w = text.split()
    for i in w:
        i = i.lower()
        if i in word:
            d[i] = d.get(i, 0) + 1
        else:
            for j in word:
                if j not in d:
                    d[j] = 0
    return d


a = popular_words('''When I was One I had just begun When I was Two I was nearly''', ['i', 'was', 'three', 'near'])
print(a)

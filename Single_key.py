# coding=utf-8
import collections


def crypt(text, key):
    column = len(key)
    alphabet_key = []
    for char in key:
        alphabet_key.append((ord(char)))

    if len(text) // column != 0:
        text += ' ' * (column - len(text) % column)
    matrix = []
    for num in range(0, column):
        matrix.append(text[num::column])

    # Делаем словарь из 2 списков
    unsorted = dict(zip(alphabet_key, matrix))
    #Сортируем по ключу и выводим строкой
    return ''.join(collections.OrderedDict(sorted(unsorted.items())).values())


def decrypt(crypted_text, key):
    column = len(crypted_text) / len(key)
    alphabet_key = []
    for char in key:
        alphabet_key.append((ord(char)))

    matrix = []
    for num in range(0, len(key)):
        matrix.append(crypted_text[num * column:(num + 1) * column:])

    unsorted = dict(zip(sorted(alphabet_key), matrix))
    text = ''
    text_list = unsorted.values()

    for item in range(len(text_list[0])):
        for num in reversed(range(0, len(key))):
            text += text_list[num][item:item + 1]

    return text


if __name__ == '__main__':
    key = 'weq'
    text = 'qwertyuoasdzxc'
    encrypted_string = crypt(text, key)
    print encrypted_string
    print decrypt(encrypted_string, key)
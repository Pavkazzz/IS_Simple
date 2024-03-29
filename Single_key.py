# coding=utf-8
import collections


def crypt(text, key):
    alphabet_key = []
    for char in key:
        alphabet_key.append((ord(char)))

    #Добавляем пробелов для ровности
    if len(text) // len(key) != 0:
        text += ' ' * (len(key) - len(text) % len(key))

    #Делим на столбцы
    matrix = []
    for num in range(0, len(key)):
        matrix.append(text[num::len(key)])

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
    text = '123456789'
    encrypted_string = crypt(text, key)
    print encrypted_string
    print decrypt(encrypted_string, key)
# coding=utf-8
import collections


def crypt(text, first_key, second_key):
    first_alphabet_key = []
    second_alphabet_key = []

    for char in first_key:
        first_alphabet_key.append((ord(char)))

    for char in second_key:
        second_alphabet_key.append((ord(char)))

    if len(text) // len(first_key) * len(second_key) != 0:
        text += ' ' * ((len(first_key) * len(second_key) - len(text)) % (len(first_key) * len(second_key)))

    matrix = []
    for num in range(0, len(first_key)):
        matrix.append(text[num::len(first_key)])

    # Делаем словарь из 2 списков
    unsorted = dict(zip(first_alphabet_key, matrix))
    #Сортируем по ключу и выводим строкой
    sorted_list = collections.OrderedDict(sorted(unsorted.items())).values()

    print sorted_list

    crypted_str = ''.join(sorted_list)
    second_matrix = []
    for num in range(len(second_key)):
        second_matrix.append(crypted_str[num::len(second_key)])

    unsorted = dict(zip(second_key, second_matrix))

    sorted_list = collections.OrderedDict(sorted(unsorted.items())).values()

    return ''.join(sorted_list)


def decrypt(crypted_text, first_key, second_key):

    column = len(crypted_text) / len(second_key)

    first_alphabet_key = []
    second_alphabet_key = []

    for char in first_key:
        first_alphabet_key.append((ord(char)))

    for char in second_key:
        second_alphabet_key.append((ord(char)))

    matrix = []
    for num in range(0, len(second_key)):
        matrix.append(crypted_text[num * column:(num + 1) * column])

    unsorted = dict(zip(sorted(first_alphabet_key), matrix))

    text_list = unsorted.values()
    text = ''
    for item in range(len(text_list[0])):
        for num in range(0, len(second_key)):
            text += text_list[num][item:item + 1]

    print text


    #Второй раз
    new_matrix = []
    column = len(crypted_text) / len(first_key)
    for num in range(len(first_key)):
        new_matrix.append(text[num * column:(num + 1) * column])

    unsorted = dict(zip(first_alphabet_key, new_matrix))
    collections.OrderedDict(sorted(unsorted.items())).values()

    text_list = collections.OrderedDict(sorted(unsorted.items())).values()

    text = ''
    for item in range(len(text_list[0])):
        for num in range(0, len(first_key)):
            text += text_list[num][item:item + 1]

    return text



if __name__ == '__main__':
    first_key = 'asdzx'
    second_key = 'wz'
    text = '1234567890 '
    encrypted_string = crypt(text, first_key, second_key)
    print encrypted_string
    print decrypt(encrypted_string, first_key, second_key)
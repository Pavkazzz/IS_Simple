# coding=utf-8
def simple_crypt(text, column=5):
    matrix = []

    if len(text) // column != 0:
        text += ' ' * (column - len(text) % column)

    for num in range(0, column):
        matrix.append(text[num::column])

    return ''.join(matrix)


def simple_decrypt(text, column=5):
    matrix = []
    for num in range(0, len(text) / column):
        matrix.append(text[num::len(text) / column])

    return ''.join(matrix)

if __name__ == '__main__':
    encrypted = simple_crypt('mpt_super12', 5)
    print encrypted
    print simple_decrypt(encrypted, 5)
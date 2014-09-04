# coding=utf-8
def simple_crypt(text, column=5):
    matrix = []
    for num in range(0, column):
        matrix.append(text[num::column])

    return ''.join(matrix)


if __name__ == '__main__':
    print simple_crypt('mpt the best', 5)
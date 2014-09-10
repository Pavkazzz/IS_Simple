import math
import random

def crypt(text):
    side = int(math.sqrt(len(text)))
    if (len(text) // side) != 0:
        side += 1

    matrix = []
    for num in range(side**2):
        index = random.randint(0, side**2)
        while matrix.__contains__(index):
            index = random.randint(0, side**2)
        matrix.append(index)

    crypted_text = [' ' for i in range(side**2+1)]
    #print crypted_text
    for num in enumerate(matrix):
        if num[0] < len(text):
            crypted_text[num[1]] = text[num[0]]

    return ''.join(crypted_text), matrix


def decrypt(text, matrix):
    encrypt = [' ' for i in range(len(matrix))]
    for char in enumerate(matrix):
        encrypt[char[0]] = text[char[1]]

    return ''.join(encrypt)

if __name__ == '__main__':
    text = 'magic square'
    text, matrix = crypt(text)
    print text
    print decrypt(text, matrix)
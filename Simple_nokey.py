def crypt(text):
    encrypted_text = []
    number_column = 5
    for row in range(0, number_column):
        encrypted_text.append(text[row::number_column])

    return ''.join(encrypted_text)


if __name__ == '__main__':
    print crypt('mpt the best')
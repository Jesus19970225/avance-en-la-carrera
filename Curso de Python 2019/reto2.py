# -*- coding: utf-8 -*-

KEYS = {
    'a': '11110000',
    'b': '11001100',
    'c': '10101010',
    'd': '01110001',
    'e': '11000101',
    'f': '00011001',
    'g': '00010110',
    'h': '11111111',
    'i': '00000000',
    'j': '11111000',
    'k': '11100000',
    'l': '10000000',
    'm': '01111111',
    'n': '00111111',
    'o': '11000000',
    'p': '11111110',
    'q': '00000001',
    'r': '00001111',
    's': '00010001',
    't': '11101110',
    'u': '10111111',
    'v': '01000000',
    'w': '00100000',
    'x': '11011111',
    'y': '11101111',
    'z': '00010000',
    'A': '00001000',
    'B': '11110111',
    'C': '11111011',
    'D': '00000100',
    'E': '11111101',
    'F': '00000010',
    'G': '11110001',
    'H': '00001110',
    'I': '11001000',
    'J': '00110111',
    'K': '11001110',
    'L': '00111110',
    'M': '00110001',
    'N': '00111001',
    'O': '11011101',
    'P': '10100000',
    'Q': '10101111',
    'R': '10110000',
    'S': '11101110',
    'T': '01111110',
    'U': '10000001',
    'V': '11000011',
    'W': '11100111',
    'X': '00111100',
    'Y': '00011000',
    'Z': '00011111',
    '0': '11100000',
    '1': '10001111',
    '2': '10001000',
    '3': '10001100',
    '4': '10001001',
    '5': '01110000',
    '6': '01111001',
    '7': '01110111',
    '8': '10110011',
    '9': '10111101',
    '.': '10110100',
    ',': '01001011',
    '?': '01001110',
    '!': '01000100',
}

def cypher(message):
    words = message.split(' ')
    binario_message = []

    for word in words:
        binario_word = ''
        for letter in word:
            binario_word += KEYS[letter]

        binario_message.append(binario_word)

    return ' '.join(binario_message)


def decipher(message):
    words = message.split(' ')
    decipher_message = []

    for word in words:
        decipher_word = ''

        letters = [word[i:i+8] for i in range(0, len(word), 8)]

        for letter in letters:

            for key, value in KEYS.items():
                if value == letter:
                    decipher_word += key

        decipher_message.append(decipher_word)

    return ' '.join(decipher_message)


def run():

    while True:

        command = str(input('''--- * --- * --- * --- * --- * --- * --- * ---

            Bienvenido a conersion a binarios. ¿Qué deseas hacer?

            [c]ifrar mensaje
            [d]ecifrar mensaje
            [s]alir
        '''))

        if command == 'c':
            message = str(input('Escribe tu mensaje: '))
            cypher_message = cypher(message)
            print(cypher_message)

        elif command == 'd':
            message = str(input('Escribe tu mensaje en binario: '))
            decypher_message = decipher(message)
            print(decypher_message)
        elif command == 's':
            print('salir')
            return False
        else:
            print('¡Comando no encontrado!')


if __name__ == '__main__':
    print('M E N S A J E S  B I N A R I O S')
    run()
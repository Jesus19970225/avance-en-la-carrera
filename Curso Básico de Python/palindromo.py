# def palindromo(palabra):
#     palabra = palabra.replace(' ', '')
#     palabra = palabra.lower()
#     palabra_invertida = palabra[::-1]
#     if palabra == palabra_invertida:
#         return True
#     else:
#         return False
palindromo = lambda palabra: palabra == palabra[::-1]


def run():
    palabra = input('Escribe una palabra: ')
    es_palindromo = palindromo(palabra)
    # if es_palindromo == True:
    if palindromo(palabra):
        print('Es palindromo')
    else:

        print('No es palindromo')


if __name__ == '__main__':
    run()
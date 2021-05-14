# -*- coding: utf-8 -*-


def run():
    word = input("Escribe una palabra: ")
    word = word.lower()
    palind(word)


def palind(word):
    drow = word[::-1]
    if drow == word:
        print("Tu palabra {} es un palindromo".format(word))
    else:
        print("Tu palabra {} NO es un palindromo".format(word))

if __name__ == '__main__':
    run()
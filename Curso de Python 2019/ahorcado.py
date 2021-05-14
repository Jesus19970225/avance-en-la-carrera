# -*- coding: utf-8 -*-
import random


IMAGES = ['''
  +---+
  |   |
      |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
      |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 /    |
      |
=========''', '''
  +---+
  |   |
  O   |
 /|\  |
 / \  |
      |
=========''']


WORDS = [
    'lavadora',
    'secadora',
    'sofa',
    'gobierno',
    'diputado',
    'democracia',
    'computadora',
    'teclado'

]


def run():
    word = random_word()
    hidden_word = ['_'] * len(word)
    tries = 0
    while True:
        display_board(hidden_word, tries)
        current_letter = str(input("Escoge una letra: "))
        letter_indexes = []
        for idx in range(len(word)):
          if word[idx] == current_letter:
            letter_indexes.append(idx)
        if len(letter_indexes) == 0:
          tries += 1
          if tries == 6:
            display_board(hidden_word, tries)
            print("")
            print("¡perdiste! La palabra correta era {}".format(word))
            break
        else:
          for idx in letter_indexes:
            hidden_word[idx] = current_letter

          letter_indexes = []
        try:
          hidden_word.index('_')
        except ValueError:
          print("")
          print("¡Felicidades! Ganaste. La palabra es: {}".format(word))
          break


def random_word():
    idx = random.randint(0, len(WORDS) - 1)
    return WORDS[idx]


def display_board(hidden_word, tries):
    print(IMAGES[tries])
    print("")
    print(hidden_word)
    print((" ___ ") * len(hidden_word))


if __name__ == '__main__':
    print('B I E N B E V E N I D O S   A   A H O R C A D O S')
    run()
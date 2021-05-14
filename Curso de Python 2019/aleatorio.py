# -*- coding: utf-8 -*-
import random

def run():
    number_found = False
    maximo = int(input("Escoje el tope de numero en el que quieras jugar: "))
    random_number = random.randint(0, maximo)

    while not number_found:
        number = int(input("Intenta un número entre 0 y el numero escojido: "))

        if number == random_number:
            print("Felicidaddes. Encontraste el número")
            number_found = True
        elif number > random_number:
            print("El numero es más pequeño")
        else:
            print("El numero es más grande")


if __name__ == '__main__':
    run()
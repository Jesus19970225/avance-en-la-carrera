import os
import random


def comparacion():
    dato = palabra(ruta ="./archivos/data.txt")
    palabra_escojida = random.choice(dato)
    lista_de_palabra_escojida = [letra for letra in palabra_escojida]
    comparacion = ["_"] * len(lista_de_palabra_escojida)
    letras_ingresadas = {}
    vidas = 7

    for i, letra in enumerate(palabra_escojida):
        if not letras_ingresadas.get(letra):
            letras_ingresadas[letra]=[]
        letras_ingresadas[letra].append(i)

    while True:
        borrarPantalla()
        print("¡Adivina la palabra!")
        for elemento in comparacion:
            print(elemento + "", end="")
        print("\n")
        logo(vidas)
        print("tienes: " + str(vidas) + " vidas.")
        print()
        letra = input("ingresa una letra: ").strip().upper()
        assert letra.isalpha(), "Solo puedes ingresar letras"

        if letra in lista_de_palabra_escojida:
            for i in letras_ingresadas[letra]:
                comparacion[i] = letra
        else:
            vidas = vidas - 1

        if "_" not in  comparacion:
            borrarPantalla()
            print("¡Ganaste la partida era", palabra_escojida)
        if vidas == 0:
            borrarPantalla()
            print ("¡Perdiste la partida!")
            logo(vidas)
            break


def logo(vidas):
    if vidas == 6:
        print('''
                +---+
                |   |
                    |
                    |
                    |
                    |
                =========''')
    elif vidas == 5:
        print('''
                +---+
                |   |
                O   |
                    |
                    |
                    |
                =========''')
    elif vidas == 4:
        print('''
                +---+
                |   |
                O   |
                |   |
                    |
                    |
                =========''')
    elif vidas == 3:
        print('''
                +---+
                |   |
                O   |
               /|   |
                    |
                    |
                =========''')
    elif vidas == 2:
        print('''
                +---+
                |   |
                O   |
               /|\  |
                    |
                    |
                =========''')
    elif vidas == 1:
        print('''
                +---+
                |   |
                O   |
               /|\  |
               /    |
                    |
                =========''')
    elif vidas == 0:
        print('''
                +---+
                |   |
                O   |
               /|\  |
               / \  |
                    |
                =========''')
    return
        

def palabra(ruta= "./archivos/data.txt"):
    with open(ruta, "r", encoding="utf-8") as f:
        opciones = []
        for line in f:
            opciones.append(line.strip().upper())
    return opciones
    comparacion( letra)


def borrarPantalla(): 
    if os.name == "posix":
        os.system ("clear")
    elif os.name == "ce" or os.name == "nt" or os.name == "dos":
        os.system ("cls")
    return
        

def run():
    comparacion()


if __name__ == '__main__':
    run()
import random


def run():
    numero_aletorio = random.randint(1, 100)
    numero_elegido = int(input ('Elige un número del 1 al 100: '))
    while numero_elegido != numero_aletorio:
        if numero_elegido < numero_aletorio:
            print('Busca un número mas grande')
        else:
            print('Busca un numero mas pequeño')
        numero_elegido = int(input('Elige otro número: '))
    print('¡Ganaste!')


if __name__ == '__main__':
    run()
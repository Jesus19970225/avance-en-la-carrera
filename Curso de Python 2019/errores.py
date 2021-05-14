# -*- coding: utf-8 -*-


def run():
    countries = {
        'mexico': 122, 'colombia': 49, 'argentina': 43, 'chile': 18, 'peru': 31
    }

    while True:
        contry = str(input('Escribe el nombre del país: ')).lower()

        try:
            print('La poblacionde {} es: {} millones'.format(contry, countries[contry]))
        except KeyError:
            print('No tenemos el dato de la población de {}'.format(contry))


if __name__ == '__main__':
    run()
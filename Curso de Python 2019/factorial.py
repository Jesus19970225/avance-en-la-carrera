# -*- coding: utf-8 -*-


def run():
    number = int(input("Escribe el número al que desea hacer factorial: "))

    result = number_factorial(number)

    print(result)


def number_factorial(number):
    if number == 0:
        return 1
    return number * number_factorial(number - 1)
    


if __name__ == '__main__':
    run()
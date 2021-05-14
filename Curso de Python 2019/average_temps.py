# -*- coding: utf-8 -*-


def run():
    temps = [21, 24, 24, 22, 20,23, 24]

    average = average_temps(temps)
    print('La temperatura promedio es: {}'.format(average))


def average_temps(temps):
    sum_of_temps = 0

    for temp in temps:
        sum_of_temps += temp

    return sum_of_temps / len(temps)


if __name__ == '__main__':
    run()
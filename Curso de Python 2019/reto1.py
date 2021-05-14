def run():
    stop = int(input("Escribe el numero hasta donde deseas sumar: "))
    respuesta = sum_rec(stop)

    print('La sumatoria recursiva dio como resultado {}'.format(respuesta))


def sum_rec(stop):
    if stop == 0:
        return 0
    
    return stop + sum_rec(stop - 1)


if __name__ == '__main__':
    run()
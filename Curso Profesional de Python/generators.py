import time


def fibo_gen(max):
    n1, n2, counter = 0, 1, 0
    while True:
        if counter == 0:
            counter += 1
            yield n1
        elif counter == 1:
            counter += 1
            yield n2
        else:
            n1, n2 = n2, n1+n2
            counter += 1
            if n2 > max:
                raise StopIteration
            else:
                yield n2


if __name__ == '__main__':
    max = int(input("¿Hasta que numero desea que la secuencia llegue?: "))
    fibonacci = fibo_gen(max)
    for element in fibonacci:
        print(element)
        time.sleep(1)
import random

def busqueda_lineal(lista, objectivo, j=0):
    match = False

    for elemento in lista:  
        j+=1
        if elemento == objetivo:
            match = True
            break

    return (match, j)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano sera la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = [random.randint(0, 100) for i in range(tamano_de_lista)]

    (encontrado, j) = busqueda_lineal(lista, objetivo)
    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'El numero de interaciones: {j}')
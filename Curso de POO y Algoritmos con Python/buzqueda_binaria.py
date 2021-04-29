import random

def busqueda_binaria(lista, comienzo, final, objetivo, j = 0):
    j+=1
    print(f'buscando {objetivo} entre {lista[comienzo]} y {lista[final - 1]}')
    if comienzo > final:
        return (False, j)

    medio = (comienzo + final)  // 2

    if lista[medio] == objetivo:
        return (True, j)
    elif lista[medio] < objetivo:
        return busqueda_binaria(lista, medio + 1, final, objetivo, j)
    else:
        return busqueda_binaria(lista, comienzo, medio - 1, objetivo, j)


if __name__ == '__main__':
    tamano_de_lista = int(input('De que tamano es la lista? '))
    objetivo = int(input('Que numero quieres encontrar? '))

    lista = sorted([random.randint(0, 100) for i in range(tamano_de_lista)])

    (encontrado, j) = busqueda_binaria(lista, 0, len(lista), objetivo)

    print(lista)
    print(f'El elemento {objetivo} {"esta" if encontrado else "no esta"} en la lista')
    print(f'El numero de interaciones: {j}')
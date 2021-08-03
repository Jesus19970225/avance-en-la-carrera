def union(my_set1, my_set2):
    my_set3 = my_set1 | my_set2
    print( "La union de los conjuntos ")
    print(my_set1)
    print(my_set2)
    print( "El resultado es: ")
    print(my_set3)


def intersection(my_set1, my_set2):
    my_set3 = my_set1 & my_set2
    print( "La intercepción de los conjuntos ")
    print(my_set1)
    print(my_set2)
    print( "Da como resultado: ")
    print(my_set3)


def difference(my_set1, my_set2):
    
    print( "La diferencia de los conjuntos ")
    print(my_set1)
    print(my_set2)
    print( "El resultado es: ")
    print(my_set1.difference(my_set2))
    print( "Y al contrario seria: ")
    print(my_set2.difference(my_set1))


def diferencia_symmetric(my_set1, my_set2):
    print( "La diferencia simetrica de los conjuntos ")
    print(my_set1)
    print(my_set2)
    print( "Da como resultado: ")
    print(my_set1.symmetric_difference(my_set2))


def run():
    my_set1 = {1, 2, 3}
    my_set2 = {3, 4, 5}
    print("Preciona 1 para union")
    print("Preciona 2 para intercepción")
    print("Preciona 3 para diferencia")
    print("Preciona 4 para diferencia simetrica")
    menu = int(input("Escoge: "))
    while menu < 1 or menu > 4:
        menu = int(input("La opcion no es valida: "))
    if menu == 1:
        union(my_set1, my_set2)
    elif menu == 2:
        intersection(my_set1, my_set2)
    elif menu == 3:
        difference(my_set1, my_set2)
    else:
        diferencia_symmetric(my_set1, my_set2)


if __name__ == '__main__':
    run()
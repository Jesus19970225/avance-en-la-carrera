opcion = int(input("""Escoje una opcion para tener la raiz cuadrada de un numero
1 Raiz cuadrada en enteros
2 Raiz cuadrada en aproximaciones
3 Busqueda binaria
"""))

def enteros():
   objetivo = int(input('Escoge un entero: '))
   respuesta = 0

   while respuesta**2 < objetivo:
        print(respuesta)
        respuesta += 1

   if respuesta**2 == objetivo:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
   else:
        print(f'{objetivo} no tiene raiz cuadrada exacta')
def aproximaciones():
    objetivo = int(input('Escoje un numero: '))
    epsilon = 0.01
    paso = epsilon**2
    respuesta = 0.0

    while abs(respuesta**2 - objetivo) >= epsilon and respuesta <= objetivo:
        respuesta += paso

    if abs(respuesta**2 - objetivo) >= epsilon:
        print(f'No se encontro la raiz cuadrada de {objetivo}')
    else:
        print(f'La raiz cuadrada de {objetivo} es {respuesta}')
def binarios():
    objetivo = int(input('Escoje un numero: '))
    epsilon = 0.001
    bajo = 0.0
    alto = max(1.0, objetivo)
    respuesta = (alto + bajo) / 2

    while abs(respuesta**2 - objetivo) >= epsilon:
        print(f'bajo={bajo}, alto={alto}, respuesta={respuesta}')
        if respuesta**2 < objetivo:
            bajo = respuesta
        else:
            alto = respuesta

        respuesta = (alto + bajo) / 2

    print(f'la raiz cuadrada de {objetivo} es {respuesta}')

if opcion == 1:
    enteros()
elif opcion == 2:
    aproximaciones()
elif opcion == 3:
    binarios()
else:
    print(f'La opcion, {opcion} no es valida por favor escoja una de las tres validas')
def conversor(tipo_pesos, valor_dolar):
    pesos = float(input("¿cuantos pesos " + tipo_pesos + " tienes?: "))
    dolares = pesos / valor_dolar
    dolares = round(dolares, 2)
    dolares = str(dolares)
    print("Tienes $" + dolares + " dolares")

menu = """
Bienvenido al conversor de monedas 💰

1 - Pesos Colombianos
2 - Pesos argentinos
3 - Pesos Mexicanos

Elige una opción: """

opcion = int(input(menu))

if opcion == 1:
    conversor("Colombianos", 3586.11)
elif opcion == 2:
    conversor("argentinos", 89.54)
elif opcion == 3:
    conversor("Mexicanos", 20.54)
else:
    print ('Ingrece una opción correpta por favor')



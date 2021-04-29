usuario_1 = input('cual es su nombre: ')
edad_usuario_1 = int(input('Cual es su edad: '))

usuario_2 = input('cual es su nombre: ')
edad_usuario_2 = int(input('Cual es su edad: '))

if edad_usuario_1 < edad_usuario_2:
    print(f'el usuario de mayor edad es ',{usuario_2})
elif edad_usuario_1 > edad_usuario_2:
    print(f'el usuario de mayor edad es ',{usuario_1})
else:
    print('Los dos usuarios tienen la misma edad')
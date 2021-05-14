# -*- coding: utf-8 -*-


def run():
    numbers = [29, 35, 39, 9, 10, 13, 17, 21, 25, 41, 43, 3, 4, 6, 47, 55, 58, 1]
    number_to_find = int(input("Ingresa un número: "))
    numbers.sort() # ordena la lista de menor a mayor

    result = binary_search(numbers, number_to_find, 0, len(numbers) - 1)
    if result is True:
        print("El número sí está en la lista.")
    else:
        print("El número No esta en la lista.")


def binary_search(numbers, number_to_find, low, high):
    if low > high:
        return False

    mid = int((low + high) / 2) 

    if numbers[mid] == number_to_find:
        return True
    elif numbers[mid] > number_to_find:
        return binary_search(numbers, number_to_find, low, mid - 1)
    else:
        return binary_search(numbers, number_to_find, mid + 1, high)




if __name__ == '__main__':
    run()
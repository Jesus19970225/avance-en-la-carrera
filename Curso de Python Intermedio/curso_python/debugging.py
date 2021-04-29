# def divisors(num):
#     try:
#         if num < 0 or num == 0:
#             raise ValueError("No se pueden ingresar numeros negativos")     
#         divisors = [i for i in range(1, num + 1) if num %  i == 0]
#         return divisors
#     except ValueError as ve:
#         print(ve)
#         return None
    

divisors = lambda num: [x for x in range(1, num + 1) if num % x == 0]

    


def run():
    try:
        num = int(input("Ingesa un numero: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()
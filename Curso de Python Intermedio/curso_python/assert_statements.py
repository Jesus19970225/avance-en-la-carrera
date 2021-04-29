# def divisors(num):
#     assert num >= 0, "El numero ingresado no puede ser negativo"
#     divisors = [i for i in range(1, num + 1) if num %  i == 0]
#     return divisors

    
divisors = lambda num: [x for x in range(1, num + 1) if num % x == 0 ]

    


def run():
    num = input("Ingesa un numero: ")
    assert num.replace("-", "").isnumeric(), "Debes ingresar un número"
    print(divisors(int(num)))
    print("Terminó mi programa")


if __name__ == '__main__':
    run()
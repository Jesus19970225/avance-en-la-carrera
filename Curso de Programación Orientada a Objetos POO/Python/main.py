from car import Car
from account import Account


def run():
    print("Hola mundo")

    car = Car("AMS234", Account("Andres Herrera", "ANDA876"))
    print(vars(car))

    car2 = Car("QWE567", Account("Andres Herrera", "ANDA876"))
    print(vars(car2))


if __name__ == '__main__':
    run()
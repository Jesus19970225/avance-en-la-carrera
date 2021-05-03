from UberX import UberX
from car import Car
from account import Account
from user import User


def run():
    print("Inicialisamos la Informacion de los carros")
    print("Car")
    car = Car("AMS234", Account("Andres Herrera", "ANDA876", "andrea@platzi.com", "2563"))
    print(vars(car))
    print(vars(car.driver))

    print("UberX")
    uberx = UberX("QWE567", Account("Andrea Ferran", "ANDA876", "andref@platzi.com", "7856"), "Chevrolet", "Spark")
    print(vars(uberx))
    print(vars(uberx.driver))

    print("User")
    user = User("Maria Valle", "SDFG125F", "mariana@platzi.com", "7856")
    print(vars(user))

if __name__ == '__main__':
    run()
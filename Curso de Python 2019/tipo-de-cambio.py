# -*- coding: utf-8 -*-

def foreign_exchage_calculator(ammount):
    mex_to_col_rate = 185.81

    return mex_to_col_rate * ammount


def run():
    print("CALCULADORA DE DIVISAS")
    print("Convierte pesos mexicanos a pesos colombianos.")
    print("")

    ammount = float(input("Ingresa la cantidad de pesos mexicanos que quieres convertir: "))

    result = foreign_exchage_calculator(ammount)

    print("${} pesos mexicanos son ${} pesos colombianos".format(ammount, result))
    print("")

if __name__ == '__main__':
     run()
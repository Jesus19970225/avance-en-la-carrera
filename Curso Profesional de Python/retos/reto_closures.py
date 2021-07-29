def make_division_by(n: int):
    assert n != 0, "No se puede dividir por cero, ya que el resultado tiende a infinito"
    """This closure returns a function that returns the division of an x number by n"""
    def division(x: int) -> int:
        return x / n
        
    return division
    

def run():
    division_by_3 = make_division_by(3)
    division_by_5 = make_division_by(5)
    division_by_18 = make_division_by(18)

    print(division_by_3(18))
    print(division_by_5(100))
    print(division_by_18(54))


if __name__ == "__main__":
    run()
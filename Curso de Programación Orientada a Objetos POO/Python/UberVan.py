from car import Car

class UberVan(Car):
    typCarAccepted = []
    seatsMaterial = []

    def __init__(self, license, driver, typCarAccepted, seatsMaterial):
        self.typCarAccepted = typCarAccepted
        self.seatsMaterial = seatsMaterial
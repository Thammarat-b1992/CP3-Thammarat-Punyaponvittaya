class Vehicle:
    lecenseCode = ""
    serialCode = ""
    def turnOnAirConditioner(self):
        print("Turn On : Air")

class Pickup(Vehicle):
    def p(self):
        print("Pickup")
    pass;

class Car(Vehicle):
    def c(self):
        print("Car")
    pass;

class Van(Vehicle):
    def v(self):
        print("Van")
    pass;

class Estatecar(Vehicle):
    def e(self):
        print("Estatecar")
    pass;

pickup = Pickup()
pickup.p()
pickup.turnOnAirConditioner()

car = Car()
car.c()
car.turnOnAirConditioner()

van = Van()
van.v()
van.turnOnAirConditioner()

estatecar = Estatecar()
estatecar.e()
estatecar.turnOnAirConditioner()
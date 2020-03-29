class Vehicle:
    DEFAULT_FUEL_CONSUMPTION = 1.25

    def __init__(self, fuel, horse_power):
        self.fuel = fuel
        self.horse_power = horse_power
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION

    def drive(self, kilometers):
        fuel_left = self.fuel - (self.fuel_consumption * kilometers)
        if fuel_left >= 0:
            self.fuel = fuel_left


class Motorcycle(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class Car(Vehicle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = 3


class RaceMotorcycle(Motorcycle):
    DEFAULT_FUEL_CONSUMPTION = 8

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


class CrossMotorcycle(Motorcycle):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class FamilyCar(Car):
    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)


class SportCar(Car):
    DEFAULT_FUEL_CONSUMPTION = 10

    def __init__(self, fuel, horse_power):
        super().__init__(fuel, horse_power)
        self.fuel_consumption = self.DEFAULT_FUEL_CONSUMPTION


moto = Motorcycle(10, 3)
print(moto.__dict__)

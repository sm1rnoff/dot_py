from abc import ABC, abstractmethod


class Vehicle(ABC):
    pass

    @abstractmethod
    def drive(self):
        pass

    @abstractmethod
    def refuel(self):
        pass


class Car(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        summer_constant =
        feasible_distance = self.fuel_quantity / self.fuel_consumption
        if distance > feasible_distance:
            return

    def refuel(self):
        pass


class Truck(Vehicle):
    def __init__(self, fuel_quantity, fuel_consumption):
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption

    def drive(self, distance):
        pass

    def refuel(self):
        pass

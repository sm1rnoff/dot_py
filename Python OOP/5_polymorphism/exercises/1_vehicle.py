from abc import ABC, abstractmethod


class Vehicle(ABC):
    @abstractmethod
    def drive(self, distance):
        pass

    @abstractmethod
    def refuel(self, fuel):
        pass


class Car(Vehicle):
    #SUMMER_CONST = 0.9

    def __init__(self, fuel_quantity, fuel_consumption):
        self.__consumption_k = 0.9
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption + \
            self.__consumption_k  # self.SUMMER_CONST

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel


class Truck(Vehicle):
    #SUMMER_CONST = 1.6

    def __init__(self, fuel_quantity, fuel_consumption):
        self.__consumption_k = 1.6
        self.fuel_quantity = fuel_quantity
        self.fuel_consumption = fuel_consumption + \
            self.__consumption_k  # self.SUMMER_CONST

    def drive(self, distance):
        fuel_needed = distance * self.fuel_consumption
        if self.fuel_quantity >= fuel_needed:
            self.fuel_quantity -= fuel_needed

    def refuel(self, fuel):
        self.fuel_quantity += fuel * 0.95


car = Car(20, 5)
car.drive(3)
print(car.fuel_quantity)
car.refuel(10)
print(car.fuel_quantity)

truck = Truck(100, 15)
truck.drive(5)
print(truck.fuel_quantity)
truck.refuel(50)
print(truck.fuel_quantity)

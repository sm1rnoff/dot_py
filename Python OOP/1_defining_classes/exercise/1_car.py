class Car:
    def __init__(self, car, model, engine):
        self.name = car
        self.model = model
        self.engine = engine

    def get_info(self):
        return f'This is {self.name} {self.model} with engine {self.engine}'

# test it here


car = Car("Kia", "Rio", "1.3L B3 I4")
print(car.get_info())

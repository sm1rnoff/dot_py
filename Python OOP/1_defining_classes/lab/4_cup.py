class Cup:
    def __init__(self, size, quantity):
        self.total = int(size)
        self.initial_amount = int(quantity)

    def fill(self, mil):
        self.initial_amount += int(mil)
        self.initial_amount = min(self.initial_amount, self.total)

    def status(self):
        return self.total - self.initial_amount


# tests starts here
cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())

class Cup:
    def __init__(self, size, quantity):
        self.total = int(size)
        self.initial_amount = int(quantity)
        self.space_left = int(size) - int(quantity)

    def fill(self, fill):
        fill_amount = int(fill)
        self.space_left -= fill_amount
        if self.space_left < 0:
            self.space_left = 0

    def status(self):
        return self.space_left


# tests starts here
cup = Cup(100, 50)
cup.fill(50)
cup.fill(10)
print(cup.status())

class Account:
    def __init__(self, id, balance, pin):
        self.__id = id
        self.balance = balance
        self.pin = pin

    def __is_correct_pin(self, pin):
        return pin == self.__pin

    @property
    def pin(self):
        return self.__pin

    @pin.setter
    def pin(self, value):
        if not value or len(str(value)) != 4:
            raise ValueError
        self.__pin = value

    def get_id(self, pin):
        if self.__is_correct_pin(pin):
            return self.__id
        return f'Wrong pin'

    def change_pin(self, old_pin, new_pin):
        if self.__is_correct_pin(old_pin):
            self.__pin = new_pin
            return f'Pin changed'
        return f'Wrong pin'

# test it below


account = Account(8827312, 100, 3421)
print(account.get_id(1111))
print(account.get_id(3421))
print(account.balance)
print(account.change_pin(2212, 4321))
print(account.change_pin(3421, 1234))

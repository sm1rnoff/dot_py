v1 = int(input())
v2 = int(input())
v3 = int(input())


def sum_numbers(v1, v2):
    """ sum first 2 integers"""
    return v1 + v2


def substract(v3):
    """ substracts 3rd integer from the sum_numbers's result"""
    return sum_numbers(v1, v2) - v3


def add_and_substract(v1, v2, v3):
    """ calls above two functions"""
    return substract(v3)


print()
print(add_and_substract(v1, v2, v3))

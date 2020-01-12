""" factorial calculation function """


def factorial(arg):
    x = int(arg)
    result = 1
    for num in range(x, 0, -1):
        result *= num
    return result


print(factorial(5))
print(factorial(4))

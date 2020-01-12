""" factorial calculation function """


def factorial(arg):
    """ Return factorial of number. """
    if arg <= 1:
        return 1
    return arg * factorial(arg - 1)


for x in range(10):
    print(f'{x}! = {factorial(x)}')

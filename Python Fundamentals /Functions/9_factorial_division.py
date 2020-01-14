v1 = int(input())
v2 = int(input())


def factorial(arg):
    """ calculate factorial of an input number """
    if arg <= 1:
        return 1
    return arg * factorial(arg - 1)


# because of Recursion Error when calculating a higher values
res1 = float(factorial(v1))
res2 = float(factorial(v2))

# output below
print(f'{res1/res2: .2f}')

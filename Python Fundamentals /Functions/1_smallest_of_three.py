val1 = int(input())
val2 = int(input())
val3 = int(input())


def minimum(val1, val2, val3):
    """ Calculates minimum number out of three input. """
    min_val = val1
    if min_val > val2:
        min_val = val2
    if min_val > val3:
        min_val = val3
    return min_val


print()
print(minimum(val1, val2, val3))

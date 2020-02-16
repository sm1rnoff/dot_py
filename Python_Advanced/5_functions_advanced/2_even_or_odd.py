def even_odd(*numbers):
    if numbers[-1] == 'even':
        return [num for num in numbers[:-1] if num % 2 == 0]
    elif numbers[-1] == 'odd':
        return [num for num in numbers[:-1] if num % 2 != 0]

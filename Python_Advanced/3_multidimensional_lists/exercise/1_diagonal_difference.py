def read_matrix_from_console():
    return [list(map(int, input().split(' '))) for _ in range(matrix_size)]


def primary_diagonal():
    the_sum = 0
    for idx in range(matrix_size):
        the_sum += matrix[idx][idx]
    return the_sum


def secondary_diagonal():
    the_sum = 0
    for idx in range(matrix_size):
        the_sum += matrix[idx][matrix_size - idx - 1]
    return the_sum


def calculation():
    if prim > sec:
        return prim - sec
    else:
        return sec - prim


matrix_size = int(input())
matrix = read_matrix_from_console()

prim = primary_diagonal()
sec = secondary_diagonal()

print(calculation())

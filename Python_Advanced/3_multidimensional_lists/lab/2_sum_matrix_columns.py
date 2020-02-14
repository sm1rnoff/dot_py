def read_matrix_from_console():
    rows, cols = map(int, input().split(', '))
    return [list(map(int, input().split(' '))) for _ in range(rows)]


#matrix = [list(map(int, input().split(' '))) for _ in range(rows)]
matrix = read_matrix_from_console()


for row in matrix:
    col_sum = 0
    for col in range(len(matrix)):
        col_sum += matrix[row][col]
    print(col_sum)

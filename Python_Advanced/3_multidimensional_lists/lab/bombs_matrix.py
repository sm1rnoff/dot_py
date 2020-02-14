rows, cols = map(int, input().split(' '))
bombs = int(input())

matrix = [[None] * cols for _ in range(rows)]  # matrix full with None-s

for _ in range(bombs):
    (row_idx, col_idx) = map(int, input().split(' '))
    matrix[row_idx][col_idx] = '* '

[print(row) for row in matrix]

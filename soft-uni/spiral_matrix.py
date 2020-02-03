def in_range(value, max_value):
    return 0 <= value < max_value


n = int(input())

row_d = [0, +1, 0, -1]
col_d = [+1, 0, -1, 0]

matrix = [[None] * n for _ in range(n)]  # fill a matrix with 'None'-s


d = 0
row = 0
col = 0

for count in range(n*n):
    matrix[row][col] = count+1
    next_row = row + row_d[d]
    next_col = col + col_d[d]
    if not in_range(next_row, n) \
            or not in_range(next_col, n) or matrix[next_row][next_col] is not None:
        d += 1
    d %= 4
    row += row_d[d]
    col += col_d[d]

[print(row) for row in matrix]

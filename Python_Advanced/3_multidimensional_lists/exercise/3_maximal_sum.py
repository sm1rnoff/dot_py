def get_matrix_input():
    return [list(map(int, input().split(' '))) for _ in range(rows)]


def sqr_check(row, col):
    sqr_sum = 0
    for r in range(row, row+3):
        for c in range(col, col+3):
            sqr_sum += matrix[r][c]
    return sqr_sum


rows, columns = map(int, input().split(' '))

matrix = get_matrix_input()

max_sum = 0
for r in range(rows - 2):
    for c in range(columns - 2):
        crnt_sum = sqr_check(r, c)
        if crnt_sum > max_sum:
            max_sum = crnt_sum
            r_idx = r
            c_idx = c

print(f'Sum = {max_sum}')

""" mtrx = ''
for r in range(r_idx, r_idx+3):
    for c in range(c_idx, c_idx+3): """

mtrx = "\n".join([" ".join([str(matrix[r][c])
                            for c in range(c_idx, c_idx+3)]) for r in range(r_idx, r_idx+3)])
print(mtrx)

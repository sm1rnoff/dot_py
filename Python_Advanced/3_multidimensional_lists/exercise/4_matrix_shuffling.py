def swaper(r1, c1, r2, c2):
    row_lst = (r1, r2)
    col_lst = (c1, c2)

    if any(val >= rows for val in row_lst):
        return print('Invalid input!')
    elif any(val >= cols for val in col_lst):
        return print('Invalid input!')

    tmp1 = matrix[r1][c1]
    tmp2 = matrix[r2][c2]
    matrix[r1][c1] = tmp2
    matrix[r2][c2] = tmp1
    print_mtrx(matrix)


def print_mtrx(mtrx):
    for row in mtrx:
        print(" ".join(list(row)))


def get_matrix_from_console():
    return [list(input().split(' ')) for _ in range(rows)]


rows, cols = map(int, input().split(' '))
matrix = get_matrix_from_console()

end = ''

while end != 'END':
    cnsl_in = input().split(' ')
    end = cnsl_in[0]
    if end == 'END':
        break
    elif cnsl_in[0] != 'swap':
        print('Invalid input!')
        continue
    elif end != 'END':
        r1, c1, r2, c2 = map(int, [cnsl_in[x] for x in range(1, 5)])

        swaper(r1, c1, r2, c2)

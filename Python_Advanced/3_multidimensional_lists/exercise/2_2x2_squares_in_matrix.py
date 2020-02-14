def get_matrix_input():
    return [list(input().split(' ')) for _ in range(rows)]


def sqr_check(row, col):
    if matrix[row][col] == matrix[row][col+1] == matrix[row+1][col] == matrix[row+1][col+1]:
        return True
    else:
        return False


rows, columns = map(int, input().split(' '))
matrix = get_matrix_input()
count = 0

for row in range(rows - 1):
    for col in range(columns - 1):
        if sqr_check(row, col):
            count += 1


print(count)

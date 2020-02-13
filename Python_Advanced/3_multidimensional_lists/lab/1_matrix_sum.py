# input
"""
3, 6
7, 1, 3, 3, 2, 1
1, 3, 9, 8, 5, 6
4, 6, 7, 9, 1, 0
"""


# desired output
"""
76
[[7, 1, 3, 3, 2, 1], [1, 3, 9, 8, 5, 6], [4, 6, 7, 9, 1, 0]]
"""

# mine wokring

rows, columns = [int(x) for x in input().split(', ')]
matrix = []
result = 0

for row in range(rows):
    print(row)
    matrix.append([])
    matrix[row] = [int(x) for x in input().split(', ')]

for row in range(rows):
    result += sum(matrix[row])

print(result)
print(matrix)


# from class


""" def read_matrix():
    rows, cols = map(int, input().split(', '))
    return [list(map(int, input().split(', '))) for _ in range(rows)]


def sum_matrix(matrix):
    the_sum = 0
    rows_count = len(matrix)

    for row_idx in range(rows_count):
        the_sum += sum(matrix[row_idx])

    return the_sum


matrix = read_matrix()
print(sum_matrix(matrix))
print(matrix) """

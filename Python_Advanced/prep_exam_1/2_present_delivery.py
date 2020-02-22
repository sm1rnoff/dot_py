"""
5
4
- X V -
- S - V
- - - -
X - - -
up
right
down
right
Christmas morning
"""


def read_matrix_from_console():
    """Reads a whole row from console and return a list of strings"""
    return [input().split(' ') for _ in range(rows)]


def matrix_print(matrix):
    """ print matrix to console row by row with space in between cells"""
    return [print(' '.join(row)) for row in matrix]


def find_santa():
    """ returns santa's coordinates"""
    for row in range(len(matrix)):
        if 'S' in matrix[row]:
            return row, matrix[row].index('S')


def nice_kids_counter():
    """ return the amount of nice kids in the matrix """
    return sum(matrix[row].count('V') for row in range(len(matrix)))

# below four defs are self explanatory


def up():
    global found, s_row, s_col, matrix
    s_row, s_col = find_santa()
    found = matrix[s_row + 1][s_col]
    matrix[s_row + 1][s_col] = 'S'
    matrix[s_row][s_col] = '-'


def down():
    global found, s_row, s_col, matrix
    s_row, s_col = find_santa()
    found = matrix[s_row - 1][s_col]
    matrix[s_row - 1][s_col] = 'S'
    matrix[s_row][s_col] = '-'


def left():
    global found, s_row, s_col, matrix
    s_row, s_col = find_santa()
    found = matrix[s_row][s_col - 1]
    matrix[s_row][s_col - 1] = 'S'
    matrix[s_row][s_col] = '-'


def right():
    global found, s_row, s_col, matrix
    s_row, s_col = find_santa()
    found = matrix[s_row][s_col + 1]
    matrix[s_row][s_col + 1] = 'S'
    matrix[s_row][s_col] = '-'


def c_found():
    pass


def v_found():
    global presents_cnt, kids
    if presents_cnt > 0:
        presents_cnt -= 1
    else:
    kids -= 1


def x_found():
    pass


def dash_found():
    pass


# get initial input
presents_cnt = int(input())
rows = int(input())
matrix = read_matrix_from_console()
kids = nice_kids_counter()
found = ''

# actions starts here
command = ''

while command != 'Christmas morning':
    command = input()
    if command == 'up':
        up()
    elif command == 'down':
        down()
    elif command == 'left':
        left()
    elif command == 'right':
        right()
    elif command == 'Christmas morning':
        break
    else:
        print(f'DEBUG: [ERROR] command = {command}')
        continue

    if found == 'X':
        x_found()
    elif found == 'V':
        v_found()
    elif found == 'C':
        c_found()
    elif found == '-':
        dash_found()
    else:
        print(f'DEBUG: [ERROR] found = {found}')

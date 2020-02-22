"""
5
4
- X V -
- S - V
- - - -
X - - -
"""


def print_mtrx(mtrx):
    """ prints an input matrix with spaces between cells"""
    for row in mtrx:
        print(' '.join(list(row)))


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
    global found, s_row, s_col
    s_row, s_col = find_santa()
    found = matrix[s_row + 1][s_col]
    matrix[s_row + 1][s_col] = 'S'
    matrix[s_row][s_col] = '-'


def down():
    global found, s_row, s_col
    s_row, s_col = find_santa()
    found = matrix[s_row - 1][s_col]
    matrix[s_row - 1][s_col] = 'S'
    matrix[s_row][s_col] = '-'


def left():
    global found, s_row, s_col
    s_row, s_col = find_santa()
    found = matrix[s_row][s_col - 1]
    matrix[s_row][s_col - 1] = 'S'
    matrix[s_row][s_col] = '-'


def right():
    global found, s_row, s_col
    s_row, s_col = find_santa()
    found = matrix[s_row][s_col + 1]
    matrix[s_row][s_col + 1] = 'S'
    matrix[s_row][s_col] = '-'

# actions in case comming across either 'C' or 'V'


def c_found():
    global presents_cnt, kids, interruption_needed
    # check up
    if matrix[s_row + 1][s_col] == 'V' or matrix[s_row + 1][s_col] == 'X':
        if presents_cnt == 0:
            interruption_needed = True
            return
        presents_cnt -= 1
        kids -= 1
        matrix[s_row + 1][s_col] == '-'
    # check right
    if matrix[s_row][s_col + 1] == 'V' or matrix[s_row + 1][s_col] == 'X':
        if presents_cnt == 0:
            interruption_needed = True
            return
        presents_cnt -= 1
        kids -= 1
        matrix[s_row + 1][s_col] == '-'
    # check left
    if matrix[s_row][s_col - 1] == 'V' or matrix[s_row + 1][s_col] == 'X':
        if presents_cnt == 0:
            interruption_needed = True
            return
        presents_cnt -= 1
        kids -= 1
        matrix[s_row + 1][s_col] == '-'


def v_found():
    global presents_cnt, kids
    presents_cnt -= 1
    kids -= 1


# get initial input
presents_cnt = int(input())
rows = int(input())
matrix = read_matrix_from_console()
kids = nice_kids_counter()
total_kids = kids
found = ''
interruption_needed = False
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

    if found == 'V':
        v_found()
    elif found == 'C':
        c_found()
    else:
        print(f'DEBUG: found = {found}')

    if interruption_needed == True:
        break

if presents_cnt == 0 and kids > 0:
    print('Santa ran out of presents!')

print_mtrx(matrix)

if kids == 0:
    print(f'Good job, Santa! {total_kids} happy nice kid/s.')
else:
    print(f'No presents for {kids} nice kid/s.')

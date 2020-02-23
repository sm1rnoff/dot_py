def read_matrix_from_console(rows):
    """Reads a whole row from console and return a list of strings"""
    return [input().split(' ') for _ in range(rows)]


def plane_finder():
    """ returns plane's coordinates"""
    for row in range(len(matrix)):
        if 'p' in matrix[row]:
            return row, matrix[row].index('p')


def target_counter():
    """ return the amount of targets in the matrix """
    return sum(matrix[row].count('t') for row in range(len(matrix)))


def should_i_go(dir, n):
    if dir == 'up':
        for x in range(n):
            if matrix[pr - x][pc] == 'x' or pr - n > 0:
                return False
            return True
    elif dir == 'down':
        for x in range(n):
            if matrix[pr + x][pc] == 'x' or pr + n < f_size:
                return False
            return True
    elif dir == 'right':
        for x in range(n):
            if matrix[pr][pc + x] == 'x' or pc + n < f_size:
                return False
        return True
    else:  # left
        for x in range(n):
            if matrix[pr][pc - x] == 'x' or pc - n > 0:
                return False
        return True


def up(act, n):
    global pr, pc
    pr, pc = plane_finder()
    if act == 'move' and should_i_go(direction, n):
        matrix[pr][pc] = '.'
        matrix[pr - n][pc] = 'p'
    elif act == 'shoot' and pr - n > 0:
        matrix[pr - n][pc] = 'x'


def down(act, n):
    global pr, pc
    pr, pc = plane_finder()
    if act == 'move' and should_i_go(direction, n):
        matrix[pr][pc] = '.'
        matrix[pr + n][pc] = 'p'
    elif act == 'shoot' and pr + n < f_size:
        matrix[pr + n][pc] = 'x'


def right(act, n):
    global pr, pc
    pr, pc = plane_finder()
    if act == 'move' and should_i_go(direction, n):
        matrix[pr][pc] = '.'
        matrix[pr][pc + n - 1] = 'p'
    elif act == 'shoot' and pc + n < f_size:
        matrix[pr][pc + n - 1] = 'x'


def left(act, n):
    global pr, pc
    pr, pc = plane_finder()
    if act == 'move' and should_i_go(direction, n):
        matrix[pr][pc] = '.'
        matrix[pr][pc - n] = 'p'
    elif act == 'shoot' and pc - n > 0:
        matrix[pr][pc - n] = 'x'


f_size = int(input())
matrix = read_matrix_from_console(f_size)

c_cntr = int(input())

targets = target_counter()

for _ in range(c_cntr):
    command_lst = []
    [command_lst.append(str) for str in list(input().split(' '))]
    action = command_lst[0]
    direction = command_lst[1]
    n = int(command_lst[2])

    if direction == 'up':
        up(action, n)
    elif direction == 'down':
        down(action, n)
    elif direction == 'right':
        right(action, n)
    else:
        left(action, n)

    del command_lst

current_targets = target_counter()


if current_targets == 0:
    print(f'Mission accomplished! All {targets} targets destroyed.')
elif current_targets != 0:
    print(f'Mission failed! {current_targets} targets left.')

for row in matrix:
    print(' '.join(row))

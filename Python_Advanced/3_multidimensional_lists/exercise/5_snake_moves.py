def str_prep():
    mltplr = rows * cols // len(snake_str)
    rmndr = rows * cols % len(snake_str)

    path = snake_str*mltplr
    for num in range(rmndr):
        path += snake_str[num]

    return path


def populate_row(r):
    global total_ch_cnt

    if r % 2 == 0:
        matrix.append([])
        for _ in range(cols):
            matrix[r].append(full_path[total_ch_cnt])
            # print(full_path[total_ch_cnt])
            total_ch_cnt += 1
    else:
        matrix.append([])
        for _ in reversed(range(cols)):
            matrix[r].append(full_path[total_ch_cnt])
            total_ch_cnt += 1
        matrix[r].reverse()


def print_mtrx_no_spaces(mtrx):
    for i in range(len(mtrx)):
        for j in range(len(mtrx[i])):
            print(mtrx[i][j], end='')
        print()


# input
rows, cols = map(int, input().split(' '))
snake_str = input()

# code execution

full_path = str_prep()
total_ch_cnt = 0
matrix = []

for r in range(rows):
    populate_row(r)

print_mtrx_no_spaces(matrix)

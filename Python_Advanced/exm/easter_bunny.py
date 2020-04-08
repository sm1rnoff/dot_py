n = int(input())
field = []
coordinates = []
eggs = 0

for row in range(n):
    line = input().split(' ')
    if 'B' in line:
        bunny_position = [row, line.index('B')]
    field.append(line)


# going right
start = bunny_position[1]
tmp_eggs = 0
c = []

for idx in range(start, n):
    if field[bunny_position[0]][idx] == 'X':
        break
    elif field[bunny_position[0]][idx] != 'B':
        tmp_eggs += int(field[bunny_position[0]][idx])
        c.append([bunny_position[0], idx])
if tmp_eggs > eggs:
    eggs = tmp_eggs
    coordinates = c
    direction = 'right'

# going left
tmp_eggs = 0
start = bunny_position[1]
c = []

for idx in range(start, -1, - 1):
    if field[bunny_position[0]][idx] == 'X':
        break
    elif field[bunny_position[0]][idx] != 'B':
        tmp_eggs += int(field[bunny_position[0]][idx])
        c.append([bunny_position[0], idx])

if tmp_eggs > eggs:
    eggs = tmp_eggs
    coordinates = c
    direction = 'left'

# going up
tmp_eggs = 0
start = bunny_position[0]
c = []

for idx in range(start, -1, - 1):
    if field[idx][bunny_position[1]] == 'X':
        break
    elif field[idx][bunny_position[1]] != 'B':
        tmp_eggs += int(field[idx][bunny_position[1]])
        c.append([idx, bunny_position[1]])

if tmp_eggs > eggs:
    eggs = tmp_eggs
    coordinates = c
    direction = 'up'

# going down
tmp_eggs = 0
start = bunny_position[0]
c = []

for idx in range(start, n):
    if field[idx][bunny_position[1]] == 'X':
        break
    elif field[idx][bunny_position[1]] != 'B':
        tmp_eggs += int(field[idx][bunny_position[1]])
        c.append([idx, bunny_position[1]])

if tmp_eggs > eggs:
    eggs = tmp_eggs
    coordinates = c
    direction = 'down'


# print result
print(direction)
[print(item) for item in coordinates]
print(eggs)

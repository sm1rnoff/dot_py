matrix = []
print("Input: ")
for x in range(3):
    matrix.append(str(input()).split(' '))

one_count = 0
two_count = 0
winner = False
print()
print("Output: ")

# check horizontal
for x in range(3):
    for y in range(3):
        if matrix[x][y] == '1':
            one_count += 1
        elif matrix[x][y] == '2':
            two_count += 1

    if one_count == 3:
        winner = True
        print("Player 1 won! ")
        break
    elif two_count == 3:
        winner = True
        print("Player 2 won! ")
        break
    else:
        one_count = 0
        two_count = 0

if winner is True:
    exit(0)

# check verticaly
for x in range(3):
    for y in range(3):
        if matrix[y][x] == '1':
            one_count += 1
        elif matrix[y][x] == '2':
            two_count += 1

    if one_count == 3:
        winner = True
        print("Player 1 won! ")
        break
    elif two_count == 3:
        winner = True
        print("Player 2 won! ")
        break
    else:
        one_count = 0
        two_count = 0

if winner is True:
    exit(0)

# check left diagonal
for x in range(3):
    if matrix[x][x] == '1':
        one_count += 1
    elif matrix[x][x] == '2':
        two_count += 1

if one_count == 3:
    winner = True
    print("Player 1 won! ")
elif two_count == 3:
    winner = True
    print("Player 2 won! ")
else:
    one_count = 0
    two_count = 0

if winner is True:
    exit(0)

# check right diagonal
if matrix[0][2] == matrix[1][1] and matrix[1][1] == matrix[2][0]:
    winner = True
    print("Player " + matrix[0][2] + " won! ")
else:
    winner = False
    print("Draw!")

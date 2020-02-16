# input
pump_count = int(input())

circle = []
starting_point = 0

# input and build 2-dim list
for x in range(pump_count):
    line_input = input()
    temp = [int(x) for x in line_input.split(' ')]
    circle.append(temp)


def check():
    """ must check if particular starting point is feasible"""
    petrol, distance = 0, 0
    for p, m in circle:
        petrol += p
        distance += m
        reach = petrol - distance
        if reach < 0:
            return False
    return True


for starting_point in range(pump_count):
    if check():
        print(starting_point)
        break

    circle.append(circle.pop(0))

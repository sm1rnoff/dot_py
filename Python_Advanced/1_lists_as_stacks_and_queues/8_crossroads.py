from collections import deque

# input
green_light = 10  # int(input())
free_window = 5  # int(input())

#action = []
action = ['Mercedes', ['Mercedes', 'BMW', 'Skoda']]
#action = [['Mercedes', 'Hummer'], ['Hummer', 'Mercedes']]
read_from_console = ''

# while read_from_console != 'END':
#    read_from_console = input()
#    action.append(read_from_console)
# action.pop()

# so far split in separate lists and all comprised in a master one which we could iterate on

#crash = False
car_count = 0
hit_at_char = 0
car = ''
green_count = len(action) - 1


def crash_in_car_pool():
    """ once split on separate pools (deque) we check for possible accidents in each and every one of them """
    green_l = green_light
    free_w = free_window
    global car_count
    global hit_at_char
    global car
    green_on = True

    pool = deque(action.pop(0))
    while pool:
        car = pool.popleft()
        car_count += 1

        green_l -= len(car)
        if green_l < 0:
            green_on = False
            free_w += green_l
            if free_w < 0:
                hit_at_char = free_w
                return True
        if green_on == False:
            return False


def result_output():
    """ gathers stats from previous def and outputs to console"""
    global green_count

    while green_count:
        green_count -= 1
        crash_in_car_pool()
        if crash_in_car_pool() == True:
            return print(f'A crash happened!\n{car} was hit at {hit_at_char}.')
    return print(f'Everyone is safe!\n{car_count} total cars passed the crossroad!')


result_output()

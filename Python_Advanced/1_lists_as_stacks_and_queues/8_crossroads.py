from collections import deque


def check_for_crashes():
    """ checks if a crash happened for a single window """
    global car_cntr, free_w, crash, car
    gr_l = green_l
    fr_w = free_w

    while car_q:
        car = car_q.popleft()
        gr_l -= len(car)
        if gr_l >= 0:
            car_cntr += 1
            continue
        elif gr_l < 0:
            fr_w -= gr_l
            if fr_w >= 0:
                car_cntr += 1
                return crash, car_cntr
            else:
                free_w = fr_w
                crash = True
                return crash, car_cntr
        else:
            return crash, car_cntr


def separate_window():
    """ builds a car queue which must get into a whole window """
    inp = ''
    while inp != 'green':
        inp = in_q.popleft()
        car_q.append(inp)
    car_q.pop()


green_l = 9  # int(input())
free_w = 3  # int(input())
in_q = deque()
cmnd = ''
car_cntr = 0
car_q = deque()
crash = False
car = ''


while cmnd != 'END':
    cmnd = input()
    in_q.append(cmnd)

while in_q:
    separate_window()
    check_for_crashes()
    if crash == True:
        break


if crash == False:
    print(f'Everyone is safe. {car_cntr} total cars passed the crossroads.')
else:
    print(f'A crash happened! {car} was hit at {car[free_w]}.')


"""
Mercedes
Hummer
green
Hummer
Mercedes
green
END
"""

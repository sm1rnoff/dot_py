# input
green_light = 10  # int(input())
free_window = 5  # int(input())

action = []
#action = ['Mercedes', 'green', 'Mercedes', 'BMW', 'Skoda', 'green']
#action = ['Mercedes', 'Hummer', 'green', 'Hummer', 'Mercedes', 'green']
read_from_console = ''

while read_from_console != 'END':
    read_from_console = input()
    action.append(read_from_console)
action.pop()

crash = False
car_count = 0
window_cnt = action.count('green')


def green_window():
    global crash
    global car_count
    global green_l
    global free_w

    green_l = green_light
    free_w = free_window

    for idx in range(action.index('green')):
        print('DEBUG action.index(green): ', action.index('green'))
        car = action[idx]
        print(f'DEBUG car: {car}')
        car_count += 1
        green_l -= len(car)
        if green_l <= 0:
            free_w += green_l
            if free_w < 0:
                print('A crash happened!')
                print(f'{car} was hit at {car[free_w]}.')
                crash = True

            # removing 'green' item in order to be ready for the next window
            action.remove('green')
            break
    action.remove('green')


for i in range(window_cnt):
    if crash == True:
        break
    green_window()

if crash != True:
    print('Everyone is safe!')
    print(f'{car_count} total cars passed the crossroad!')

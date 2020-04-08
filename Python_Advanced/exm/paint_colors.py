from collections import deque
#from math import floor

main = ['red', 'yellow', 'blue']
secondary = ['orange', 'purple', 'green']

input_str = deque(input().split(' '))
#input_str = deque('r ue nge ora bl ed'.split(' '))
#input_str = deque('re ple blu pop e pur d'.split(' '))

color_list = []
secondarys = deque([])


while input_str:
    if len(input_str) != 1:
        first = input_str.popleft()
        last = input_str.pop()
        possible_color = first+last
        reversed_possible_color = last+first
    else:
        possible_color = input_str.popleft()
        reversed_possible_color = ''

    if possible_color in main:
        color_list.append(possible_color)
        continue
    elif reversed_possible_color in main:
        color_list.append(reversed_possible_color)
        continue
    elif possible_color in secondary:
        color_list.append(possible_color)
        continue
    elif reversed_possible_color in secondary:
        color_list.append(reversed_possible_color)
        continue

    if len(input_str) == 0:
        break
    mid_idx = round(len(input_str)/2)
#    mid_idx = floor(len(input_str)/2)
    input_str.insert(mid_idx, first[:-1] + last[:-1])

for color in color_list:
    if color == 'orange':
        if 'red' not in color_list or 'yellow' not in color_list:
            color_list.remove(color)
    elif color == 'purple':
        if 'red' not in color_list or 'blue' not in color_list:
            color_list.remove(color)
    elif color == 'green':
        if 'blue' not in color_list or 'yellow' not in color_list:
            color_list.remove(color)

print(color_list)

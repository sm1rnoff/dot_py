from collections import deque

# get input and declare variables
boxes = deque([int(item) for item in input().split(' ')])
magics = deque([int(item) for item in input().split(' ')])
fail = True

cost_table = {150: 'Doll', 250: 'Wooden train',
              300: 'Teddy bear', 400: 'Bicycle'}
present_ready = {'Doll': 0, 'Wooden train': 0, 'Teddy bear': 0, 'Bicycle': 0}

# logic
while len(boxes) != 0 and len(magics) != 0:
    combined = boxes[-1] * magics[0]
    if boxes[-1] * magics[0] in cost_table.keys():
        present_ready[cost_table[combined]] += 1
        boxes.pop()
        magics.popleft()
    else:
        if combined < 0:
            comb_sum = boxes[-1] + magics[0]
            boxes.pop()
            magics.popleft()
            boxes.append(comb_sum)
        elif combined > 0:
            magics.popleft()
            boxes[-1] += 15
        else:
            if magics[0] == 0:
                magics.popleft()
            elif boxes[-1] == 0:
                boxes.pop()
            else:
                boxes.pop()
                magics.popleft()

if present_ready['Doll'] != 0 and present_ready['Wooden train'] != 0:
    print('The presents are crafted! Merry Christmas!')
    if len(boxes) != 0:
        print('Materials left: ', end='')
        print(', '.join(str(num) for num in boxes))
    if len(magics) != 0:
        print('Materials left: ', end='')
        print(', '.join(str(num) for num in magics))
    [print(f'{key}: {present_ready[key]}')
     for key in present_ready if present_ready[key] != 0]
elif present_ready['Teddy bear'] != 0 and present_ready['Bicycle'] != 0:
    print('The presents are crafted! Merry Christmas!')
    if len(boxes) != 0:
        print('Materials left: ', end='')
        print(', '.join(str(num) for num in boxes))
    if len(magics) != 0:
        print('Materials left: ', end='')
        print(', '.join(str(num) for num in magics))
    [print(f'{key}: {present_ready[key]}')
     for key in present_ready if present_ready[key] != 0]
else:
    print('No presents this Christmas!')
    if len(boxes) != 0:
        print('Materials left: ', end='')
        print(', '.join(str(num) for num in boxes))
    if len(magics) != 0:
        print('Materials left: ', end='')
        print(', '.join(str(num) for num in magics))
    [print(f'{key}: {present_ready[key]}')
     for key in present_ready if present_ready[key] != 0]

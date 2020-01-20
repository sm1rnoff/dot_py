from collections import deque

# input
total_amount = int(input())
line = input()

# build a queue with all customers
queue = deque([int(x) for x in line.split(' ')])

# find the max
maximum_value = 0
for x in queue:
    if maximum_value < x:
        maximum_value = x
print(maximum_value)

while queue and total_amount >= queue[0]:
    total_amount -= queue.popleft()

if queue:
    left = ''
    while queue:
        left += str(queue.popleft())+' '
    print(f'Orders left: {left}')
else:
    print('Orders complete')

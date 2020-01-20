from collections import deque

# input
line1 = input()  # 5 2 13
line2 = input()  # 1 13 45 32 4

# actual work
cnt = int(line1.split(' ')[0])
rem = int(line1.split(' ')[1])
el = int(line1.split(' ')[2])

# create stack of integers from second line input
q = deque([int(x) for x in line2.split(' ')])

# remove from queue
for x in range(rem):
    q.popleft()

# output
if el in q:
    print(True)
elif len(q) == 0:
    print(0)
else:
    smallest = q[0]
    for i in range(1, len(q)):
        if smallest > q[i]:
            smallest = q[i]
    print(smallest)

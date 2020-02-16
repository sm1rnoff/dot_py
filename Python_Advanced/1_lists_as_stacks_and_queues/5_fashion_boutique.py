# input
line1 = input()
rack_size = int(input())

box_stack = [int(x) for x in line1.split(' ')]

rack_counter = 1
current_rack = rack_size

while box_stack:
    if current_rack < box_stack[-1]:
        rack_counter += 1
        current_rack = rack_size
    else:
        current_rack -= box_stack[-1]
        box_stack.pop()

# output
print(rack_counter)

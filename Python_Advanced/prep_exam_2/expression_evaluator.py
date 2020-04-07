from collections import deque
import math

input_str = deque(input().split(' '))
digits_so_far = deque([])


def star(lst):
    temp_result = lst.popleft()
    while lst:
        temp_result *= lst.popleft()
    return temp_result


def plus(lst):
    temp_result = lst.popleft()
    while lst:
        temp_result += lst.popleft()
    return temp_result


def minus(lst):
    temp_result = lst.popleft()
    while lst:
        temp_result -= lst.popleft()
    return temp_result


def fwd_slash(lst):
    temp_result = lst.popleft()
    while lst:
        temp_result /= lst.popleft()
        temp_result = math.floor(temp_result)
    return temp_result


while input_str:
    chr = input_str.popleft()
    if chr == '*':
        result = star(digits_so_far)
        digits_so_far.appendleft(result)
        continue
    elif chr == '+':
        result = plus(digits_so_far)
        digits_so_far.appendleft(result)
        continue
    elif chr == '-':
        result = minus(digits_so_far)
        digits_so_far.appendleft(result)
        continue
    elif chr == '/':
        result = fwd_slash(digits_so_far)
        digits_so_far.appendleft(result)
        continue

    digits_so_far.append(int(chr))

print(digits_so_far.pop())

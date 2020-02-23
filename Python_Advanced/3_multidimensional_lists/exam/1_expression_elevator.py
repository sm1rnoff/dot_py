from collections import deque
import operator

input_str = '10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *'
# in_lst = list(input().split(' '))
# '10 23 * 4 2 / 30 10 + 100 50 - 2 -1 *'
# 0  1  2 3 4 5  6 7  8 9  10 11 12 13 14
# 230 4 2 / 30 10 + 100 50 - 2 -1 *'

in_lst = deque(input_str.split(' '))
var_lst = deque()
opr_lst = ('*', '+', '-', '/')


def calculation(opr, var_lst):
   if opr == '*':
        while var_lst:
            return result *= var_lst.popleft()
    elif opr == '+':
       while var_lst:
            return result += var_lst.popleft()
    elif opr == '-':
        while var_lst:
            return result -= var_lst.popleft()
    else:
        while var_lst:
            return result /= var_lst.popleft()


while in_lst:
    digit = in_lst.popleft()
    if digit not in opr_lst:
        var_lst.append(int(digit))
    elif digit == '*'


map()

multiplier = int(input())
int_list = list(map(int, [str for str in input().split(' ')]))

int_list = list(map(lambda x: x * multiplier, int_list))
print(' '.join(map(str, int_list)))

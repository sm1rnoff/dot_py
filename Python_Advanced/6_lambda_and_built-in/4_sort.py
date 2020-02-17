num_list = list(map(int, input().split(' ')))
num_list = list(filter(lambda x: x < 0, num_list))
print(abs(sum(num_list)))

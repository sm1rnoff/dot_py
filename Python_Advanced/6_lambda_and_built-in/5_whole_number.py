# You will receive a list of numbers. Round every number and print the
#  total sum multiplied by the length of the initial list.
# input
# 4.3 5.6 5.5 1.2 7.9
# exptected output
# 125

num_list = list(map(float, input().split(' ')))
num_list = list(map(lambda num: round(num), num_list))

print(sum(num_list) * len(num_list))

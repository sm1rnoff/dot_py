# You will receive a list of numbers. Round the numbers, print the min and max and multiply the numbers by 3.
# Print only the unique numbers in ascending order separated by space.
# input
# 7 9 15 432 1.2 0.2 0.5 1 6


def remove_duplicates(num):
    if num in result:
        return False
    result.append(num)
    return True


result = []

num_list = list(map(float, input().split(' ')))

num_list = map(lambda num: round(num), num_list)

num_list = filter(remove_duplicates, num_list)

num_list = sorted(num_list)

print(min(num_list))
print(max(num_list))

num_list = list(map(lambda num: num * 3, num_list))

print(' '.join(str(num) for num in num_list))

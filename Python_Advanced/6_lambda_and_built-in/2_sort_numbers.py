input_str = input()
num_list = []

[num_list.append(str) for str in input_str.split(' ')]
lst_lenght = len(num_list)

num_list = sorted(
    list(map(int, filter(lambda item: item.isdigit(), num_list))))

num_list = list(filter(lambda x: x > lst_lenght, num_list))

print(' '.join(map(str, num_list)))

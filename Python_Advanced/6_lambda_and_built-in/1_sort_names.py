names_list = []
[names_list.append(name) for name in input().split(' ')]

print(' '.join(sorted(names_list, reverse=True)))

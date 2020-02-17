names_list = []
[names_list.append(name) for name in input().split(' ')]

#name_list = sorted(names_list, reverse=True)

#print(' '.join(name_list))

print(' '.join(sorted(names_list, reverse=True)))

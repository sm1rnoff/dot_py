# You will receive a list of names. Filter the bad names and print the
# total sum of the length of the names. A valid name is a name that starts
# with an uppercase letter and the rest is in lower case.

# Pesho Gosho staMaT PresLav Stefan Martin

# expected output 22

name_list = list(input().split(' '))

name_list = list(filter(lambda name: name == name.capitalize(), name_list))

total_lenght = 0

total_lenght = sum(list(map(lambda name: len(name), name_list)))

print(total_lenght)

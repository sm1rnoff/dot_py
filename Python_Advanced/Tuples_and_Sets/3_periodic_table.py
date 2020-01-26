n = int(input())
chemical_stuff = set()

[chemical_stuff.update(input().split(' ')) for _ in range(n)]

for element in chemical_stuff:
    print(element)

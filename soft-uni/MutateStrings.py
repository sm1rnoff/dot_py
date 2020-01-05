print("Input: ")
first = input()
second = input()

print()
print('Output :')

for x in range(0, len(first)):
    if first[x] != second[x]:
        result = second[:x] + first[x:]
        if result != first:
            print(result)

print(second)

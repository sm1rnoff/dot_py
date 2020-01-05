num = input("Please add a number: ")
result = int(num)
distinct = False

# print("[DEBUG]: ", result)
while distinct is False:
    distinct = True
    for x in range(0, len(num) - 1):
        for y in range(x + 1, len(num)):
            if int(num[x]) == int(num[y]):
                distinct = False
    if distinct is False:
        result += 1
        num = str(result)

print("Next happy year is: ", result)

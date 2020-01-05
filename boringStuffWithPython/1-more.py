userin = '872356'

# try /except

# list = [int(x) for x in str(num)]
# max(list)

list = []

for x in userin:
    print("[DEBUG] x : ", x)
    for y in userin:
        print("[DEBUG] y : ", y)
        if int(x) >= int(y):
            list.insert(0, x)
            print("[DEBUG] list : ", list)
            break

print(list)

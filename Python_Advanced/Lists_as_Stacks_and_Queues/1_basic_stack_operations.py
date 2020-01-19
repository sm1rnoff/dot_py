# input
line1 = input()  # 5 2 13
line2 = input()  # 1 13 45 32 4

# actual work
cnt = int(line1.split(' ')[0])
rem = int(line1.split(' ')[1])
elem = int(line1.split(' ')[2])

# create stack of integers from second line input
st = [int(x) for x in line2.split(' ')]

# pop
for x in range(rem):
    st.pop()

if elem in st:
    print(True)
elif len(st) == 0:
    print(0)
else:
    smallest = st[0]
    for i in range(1, len(st)):
        if smallest > st[i]:
            smallest = st[i]
    print(smallest)


# output

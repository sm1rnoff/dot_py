n = int(input())
usernames = set([input() for _ in range(n)])

for username in usernames:
    print(username)

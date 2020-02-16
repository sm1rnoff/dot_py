n, m = [int(x) for x in input().split(' ')]

n_set = set([input() for _ in range(n)])
m_set = set([input() for _ in range(m)])

for value in n_set & m_set:
    print(value)

#not done


def find_strongest_eggs(*test):
    seq, num = test
    avg = len(seq) / float(num)
    out = []
    last = 0.0

    while last < len(seq):
        out.append(seq[int(last):int(last + avg)])
        last += avg

    return [max(out[n]) for n in range(num)]


print(find_strongest_eggs([-1, 7, 3, 15, 2, 12], 2))

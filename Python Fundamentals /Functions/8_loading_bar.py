v1 = int(input())
load = int(v1/10)


def loading_bar(arg):
    bar = ''
    for x in range(arg):
        bar += '%'
    for x in range(10 - arg):
        bar += '.'
    return bar


if v1 == 100:
    print(f'{v1} Complete!')
    print(f'[{loading_bar(load)}]')
else:
    print(f'{v1}% [{loading_bar(load)}]')
    print('Still loading...')

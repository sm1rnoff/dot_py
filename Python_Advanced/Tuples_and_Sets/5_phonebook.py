phonebook = {}
record = ''
while record != 'search':
    record = input()
    if record != 'search':
        temp = record.split('-')
        phonebook[temp[0]] = temp[1]

name = ''

while name != 'stop':
    name = input()
    if name == 'stop':
        break
    elif name in phonebook:
        print(f'{name} -> {phonebook[name]}')
    else:
        print(f'Contact {name} does not exist.')

dictionary = {'name': 'Peter', 'age': 25, 'key': 'another value'}


def kwargs_length(**kwargs):
    return len(kwargs)


print(kwargs_length(**dictionary))

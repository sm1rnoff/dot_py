x = "global"


def outer():

    x = "local"

    def inner():
        nonlocal x  # fix added to initial code
        x = "nonlocal"
        print("inner:", x)

    def change_global():
        global x  # fix added to initial code
        x = "global: changed!"

    print("outer:", x)
    inner()
    print("outer:", x)
    change_global()


print(x)
outer()
print(x)

"""
global
outer: local
inner: nonlocal
outer: nonlocal
global: changed!
"""

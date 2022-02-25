# LEGB
# Local Enclosing Global BuiltIn
x = 'global x'


def inner():
    global x
    x = 'inner x'
    print(x)


# inner()
# print(x)


def outer():
    x = 'outer x'

    def inner1():
        nonlocal x  # local x of the enclosing function : this is used to chg the value not globally but within
        x = 'inner x'
        print(x)
    inner1()
    print(x)


outer()

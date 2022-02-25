def hello_func():  # used to define a function
    pass  # can be used if you do not want the function to do anything for now


print(hello_func())  # call the function

# DRY -DONT REPEAT YOURSELF


def hello_func2():
    print('Hello World!')


hello_func2()

# FUNCT RETURNING VALUES


def hello_func3():
    return 'Hello Function!'


print(hello_func3())

# since string is retuned we can use string methods here
print(hello_func3().upper())

# function with passing arguement


def hello_func4(greeting, name='You'):
    return '{}, {}.'.format(greeting, name)


print(hello_func4('HI'))
print(hello_func4('HI', 'Suba'))

# positional and keyword  arguements : number of arguement


def student_info(*args, **kwargs):  # any number of arguement
    print(args)
    print(kwargs)


student_info('Math', 'Art', name='Suba', age='38')
student_info('Dance', name='Mith', age='5', sex='M')

courses = ['Math', 'Art']
info = {'name': 'Mith', 'age': '5', 'sex': 'M'}

print('course and info passed to only args')
student_info(courses, info)

print('course and info passed to args and kwargs')
student_info(*courses, **info)

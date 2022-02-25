class Employee:

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@company.com'
        self.pay = pay

    def fullname(self):  # Method to get FullNAme (self shd be passed)
        return '{} {}'.format(self.first, self.last)

    # Dunder method mostly used for other developers who use this class __methodname__ is called dunder
    def __repr__(self):
        return "Employee('{}', '{}', {})".format(self.first, self.last, self.pay)

    # for end user
    def __str__(self):
        return '{} - {}'.format(self.fullname(), self.email)

    def __add__(self, other):
        return self.pay + other.pay

    # dunder method to cal the length of the full name
    def __len__(self):
        return len(self.fullname())


emp1 = Employee('Suba', 'Jana', 50000)
emp2 = Employee('Suba', 'Jana', 60000)

print(emp1)  # if repr is only present it will called or if both present then only str will be called
# to call each specifically
print(repr(emp1))
print(str(emp1))


print(1+2)
print(int.__add__(1, 2))
print(str.__add__('a', 'b'))

print(emp1 + emp2)  # this will call the dunder add method to add 2 employees salary
print(len(emp1))

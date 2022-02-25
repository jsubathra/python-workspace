# Property Decorators
class Employee:
    def __init__(self, first, last):
        self.first = first
        self.last = last
        # Uncomment for eg1
        # self.email = first + '_'+last + '@gmail.com'

    # Property Getters
    @property  # to access email as an attribute  instead of a method we add this decorator
    def email(self):
        return '{}.{}'.format(self.first, self.last)

    # Property Getters
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)

    # Property Setter
    @fullname.setter  # This is the setter method
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last

    # Property Deletor
    @fullname.deleter
    def fullname(self):
        print('Delete name!')
        self.first = None
        self.last = None


emp_1 = Employee('suba', 'jana')
emp_1.fullname = 'Divya Jana'  # This can be done with Setters

# emp_1.first = 'Suba1'
print(emp_1.first)
# Email added as a property so the change rweflects everywhere. Also user code need not change
print(emp_1.email)
print(emp_1.fullname)

# to call the deleter
del emp_1.fullname


# eg1
# print(emp_1.first)
# # email does not reflect the changed first name as constructor called once instance created and email is assignd
# #you can use prop decorators to do like that
# print(emp_1.email)
print(emp_1.fullname)

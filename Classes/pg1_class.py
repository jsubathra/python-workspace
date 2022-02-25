# OOPS in PY
# Class is blueprint and instance contain data unique to instance
class Employee:

    raise_amount = 1.04
    num_of_employee = 0
    # Self is the instance , by defaut we need to pass and init is the constructor

    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.email = first + '_' + last + '@company.com'
        self.pay = pay
        # this class varibale is for the class itself and not for instance
        Employee.num_of_employee += 1
        # we do not want this varible to change and give diff value for each instance

    def fullname(self):  # Method to get FullNAme (self shd be passed)
        return '{} {}'.format(self.first, self.last)

    def apply_raise(self):
        # should access class variable using self or class name
        self.pay = int(self.pay * self.raise_amount)

    # this is the class method and we pass cls and add decorator @classmethod
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount


print(
    f'Number of Employee before creating instance: {Employee.num_of_employee}')
# Self passesd by default ...calling using instance
emp1 = Employee('Suba', 'Jana', 50000)
emp2 = Employee('Kar', 'Ama', 60000)

print(
    f'Number of Employee after creating instance: {Employee.num_of_employee}')

print(emp1.num_of_employee)

# Self is passed by default when calling method through instance
print(emp1.fullname())
# WHen calling through class then we need to pass the instance in place of self
print(Employee.fullname(emp1))
print(emp1.pay)

# to get the  namespace but the instance will not give the class variabe raise_amount
print(emp1.__dict__)
# to get the  namespace but the instance will give the class variabe raise_amount
print(Employee.__dict__)

# Employee.raise_amount = 1.05  # this will chg the instance and class raise_anount
# print(Employee.raise_amount)
# print(emp1.raise_amount)

emp1.raise_amount = 1.05
# the class variable will be 1.04 only and only emp1 will have hte changed value
print(Employee.raise_amount)
print(emp1.raise_amount)

Employee.set_raise_amt(1.05)
print(Employee.raise_amount)
print(emp1.raise_amount)
print(emp2.raise_amount)

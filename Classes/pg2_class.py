import datetime


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

    # alternative constructor
    @classmethod
    def from_string(cls, emp_string):
        first, last, pay = emp_string.split('-')
        return cls(first, last, pay)

    # Static Methods don't operate on instance or class
    @staticmethod
    def is_work_day(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True


emp_1 = Employee.from_string('John-Adam-70000')
my_date = datetime.date(2021, 1, 1)
print(Employee.is_work_day(my_date))
print(emp_1.fullname())


# SubClass
class Developer(Employee):
    raise_amount = 1.10

    def __init__(self, first, last, pay, prog_lang):
        # call the parent class init method to handle
        super().__init__(first, last, pay)
        # Employee.__init__(self,first,last,pay)
        self.prog_lang = prog_lang


# print(help(Developer))  # Gives the Nethod Resolution Order
dev1 = Developer('Suba', 'Jana', 50000, 'Python')
dev2 = Developer('Suba1', 'Jana1', 60000, 'Java')
print(dev1.fullname())
print(dev2.prog_lang)

# Subclass


class Manager(Employee):
    # list is always passed as none and then assigned
    def __init__(self, first, last, pay, employees=None):
        super().__init__(first, last, pay)
        if employees is None:
            self.employees = []
        else:
            self.employees = employees

    def add_employee(self, emp):
        if emp not in self.employees:
            self.employees.append(emp)

    def remove_employee(self, emp):
        if emp in self.employees:
            self.employees.remove(emp)

    def print_empl(self):
        for emp in self.employees:
            print('--->', emp.fullname())


mgr = Manager('Sue', 'Smith', 80000, [dev1, dev2])
print(mgr.fullname())
print(mgr.print_empl())


print(isinstance(Manager, Employee))
print(isinstance(Manager, Developer))
print(isinstance(Manager, Manager))
print('########')
print(issubclass(Manager, Employee))
print(issubclass(Manager, Developer))
print(issubclass(Manager, Manager))

class Employee:
    __cprt = 0
    _count = 0
    def __init__(self):
        Employee._count = Employee._count + 1

    def display(self):
        print('number of employee', Employee._count)


emp = Employee()

emp1 = Employee()

emp.display()
print(emp._count)
print(emp._cprt)

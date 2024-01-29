#!/usr/bin/python3
class Emp:
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + "-" + last + '@gmail.com'

    def fullname(self):
        return '{} {}'. format(self.first, self.last)

emp_1 = Emp('Lumasia', 'Stan', 60000)
emp_2 = Emp('Emma', 'Munde', 80000)

print(Emp.fullname(emp_1))

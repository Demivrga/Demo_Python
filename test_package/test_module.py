'''
Created on Jan 4, 2017

@author: Isaac
'''

class Employee:
    
    num_of_emps = 0
    raise_amount = 1.04
    
    def __init__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@test.com'
        
        Employee.num_of_emps += 1
        
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    def apply_raise(self):
        self.pay = int(self.pay * self.raise_amount)
        
    @classmethod
    def set_raise_amount(cls, amount):
        cls.raise_amount = amount
        
    
    @classmethod
    def from_string(cls, emp_str, parser):
        first, last, pay = emp_str.split(parser)
        return cls(first, last, pay)
    
    @staticmethod
    def is_workday(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False
        return True

emp_1 = Employee('Isaac', 'Greer', 50000)
emp_2 = Employee('Cloud', 'Chaser', 60000)

print(emp_1.email)
print(emp_2.email)
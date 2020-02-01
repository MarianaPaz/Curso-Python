# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:34:53 2020

@author: CEC
"""

class Employee:
    'Common base class for all employees'
    empCount = 0
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        Employee.empCount += 1
        
    def displayCount(self):
        print("Total Employee %d" % Employee.empCount)
        
    def displayEmployee(self):
        print("Name:", self.name, ", Salary:", self.salary)
        
"This would create first object of Employee class"
emp1 = Employee("Zara",2000)
"This would create second object of Employee class"
emp2 = Employee("Manni",5000)
"This would create 3 object of Employee class"
emp3 = Employee("Kevin",15000)
"This would create 4 object of Employee class"
emp4 = Employee("Victor",16000)
emp1.displayEmployee()
emp2.displayEmployee()
emp3.displayEmployee()
emp4.displayEmployee()
emp4.displayCount()
print("Total Employee %d" % Employee.empCount )


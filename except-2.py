# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:30:36 2020

@author: CEC
"""

try:
    y=1/0
    print(y)
except ZeroDivisionError:
    print("Zero Division")
except ArithmeticError:
    print("Arithmetic problem")

print("THE END")
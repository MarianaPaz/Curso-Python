# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:21:44 2020

@author: CEC
"""

try:
    x=int(input("Enter a number:"))
    y=1/x
    print(y)
except ZeroDivisionError:
    print("You cannot divide by zero, sorry")
except ValueError:
    print("You must enter an integer value")
except:
        print("Oh dear, something went wrong")
print("THE END")
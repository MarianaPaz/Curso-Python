# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:34:28 2020

@author: CEC
"""
def badFun(n):

    try:
        return 1/n
    except ArithmeticError:
        print("Arithmetic problem")
    return None

badFun(0)
print("THE END")
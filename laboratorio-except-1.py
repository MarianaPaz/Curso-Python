# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 18:45:59 2020

@author: CEC
"""

def readint(prompt,min,max):
    try:
        x = int(input("Ingrese el número:"))
        
        if x>= min  and x<=max:
            return x
        assert (x < min  and x>max), "The value is not within permitted range (-10..10)"
                  
    except ValueError:
        return "wrong input "
    
    
    
    
    
v = readint("Enter a number from -10 to 10: ", -10, 10)
print("The number is:", v)
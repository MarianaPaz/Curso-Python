# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:26:14 2020

@author: CEC
"""

file=open("data/devices.txt","a")
while True:
    newItem = input("Ingrese un nuevo dispositivo:")
    if newItem == "exit":
        break
    else:
        file.write(newItem +"\n")
file.close()

file=open("data/devices.txt","r")
for item in file:
    print(item)
file.close()
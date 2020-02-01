# -*- coding: utf-8 -*-
"""
Created on Sat Feb  1 09:16:35 2020

@author: CEC
"""
"""
file=open("data/devices.txt","r")
for item in file:
    print(item)
file.close()
"""
"""
file=open("data/devices.txt","r")
for item in file:
    item=item.strip()
    print(item)
file.close()
"""

devices=[]
file=open("data/devices.txt","r")
for item in file:
    item=item.strip()
    devices.append(item)
file.close()
print(devices)
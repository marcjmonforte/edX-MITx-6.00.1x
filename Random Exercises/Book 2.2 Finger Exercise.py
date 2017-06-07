#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  2 13:46:41 2017

@author: mmonforte
"""

myList = [5,11,7]
largest = 0

for num in myList:
    if num % 2 != 0:
        if num > largest:
            largest = num
            
print('The largest odd number is ', largest, '.')
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 22:41:10 2017

@author: mmonforte
"""

"""
Finger exercise: Let s be a string that contains
    a sequence of decimal numbers separated by commas,
    e.g., s = '1.23, 2.4, 3.123'. Write a program
    that prints the sum of the numbers in s.
"""

s = '1.23, 2.4, 3.123'
l = [float(x) for x in s.split(',')]
total = 0

for num in l:
    total = total + num
    
print(num)
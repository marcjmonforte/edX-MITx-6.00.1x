#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 20:48:40 2017

@author: mmonforte
"""

#Find the cube root of a perfect cube
x = int(input('Enter an integer: '))
ans = 0

while ans**3 < abs(x):
    ans = ans + 1

if ans**3 != abs(x):
    print(x, 'is not a perfect cube.')
else:
    if x < 0:
        ans = -ans
    print('Cube root of', x, 'is', ans, '.')
    
print('Value of the decrementing function abs(x) - ans**3 is', 
      abs(x) - ans**3)
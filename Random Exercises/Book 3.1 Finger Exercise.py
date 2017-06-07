#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun  4 21:02:27 2017

@author: mmonforte
"""

# Ask user for an integer.
num = int(input('Enter an integer: '))

# Print two integers: 'root' and 'pwr'

root, pwr = 0, 1

# pwr must be: 0 < pwr < 6
# root**pwr must equal integer from user

while root**pwr != num:
    root = root + 1
    for i in range(1,6):
        if root**i == num:
            pwr = i
            break        

# If root**pwr != num, print a message to that effect.
print('Root: ', root)
print('Exponent: ', pwr)
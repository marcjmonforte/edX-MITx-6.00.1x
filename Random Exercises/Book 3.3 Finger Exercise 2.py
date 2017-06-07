#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 22:12:15 2017

@author: mmonforte
"""

"""
Finger Exercise:
    What would have to be changed to make code work
    for finding approximation for cube root?
    What about both positive and negative?
"""

x = -125
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, abs(x))
ans =(high + low)/2.0

if x < 0:
    x = abs(x)
while abs(ans**3 - x) >= epsilon:
    print('low =', low,
          'high =', high,
          'ans =', ans)
    numGuesses += 1
    if ans**3 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
        
print('numGuesses =', numGuesses)
print(ans, 'is close to the cube root of', x)

"""
Answer:
    Change the validation test for cubes instead of squares
    For negatives, just convert to positive before executing.
    This doesn't take into account imaginary/complex numbers.
"""
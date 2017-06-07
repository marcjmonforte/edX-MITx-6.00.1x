#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 21:40:31 2017

@author: mmonforte
"""

"""
Finger Exercise:
    What would the code below do if x were -25 instead of 25?
"""

x = 25
epsilon = 0.01
numGuesses = 0
low = 0.0
high = max(1.0, x)
ans =(high + low)/2.0

while abs(ans**2 - x) >= epsilon:
    print('low =', low,
          'high =', high,
          'ans =', ans)
    numGuesses += 1
    if ans**2 < x:
        low = ans
    else:
        high = ans
    ans = (high+low)/2.0
    
print('numGuesses =', numGuesses)
print(ans, 'is close to the square root of', x)

"""
Result of switching to -25:
    high value continually shrinks, low value never updates
    instead of reaching a number that when squared would equal x
        continually shrink into infinite loop
    
Why it works remaining as 25:
    "high" and "low" values both closing the gap on square root with each iteration
    eventually will hit a number close to true square root of x    
"""
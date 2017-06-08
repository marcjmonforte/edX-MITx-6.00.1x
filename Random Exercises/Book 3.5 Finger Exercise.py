#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun  7 23:13:18 2017

@author: mmonforte
"""

"""
Finger Exercise:
    Add some code to the implementation of the Newton-Raphson that
    keeps track of the number of iterations used to find the root.
    Use that code as part of a program that compares the efficiency of
    the Newton-Raphson and bisection search.
    Spoilers: Newton-Raphson should be more efficient.
"""

# Newton-Raphson for square root
# Find x such that x**2 - 24 is within epsilon of 0

def newton_raphson():
    epsilon = 0.01
    k = 24.0
    guess = k / 2.0
    counter = 0
    
    while abs(guess * guess - k) >= epsilon:
        guess = guess - (((guess ** 2) - k) / (2 * guess))
        counter += 1
    print('Square root of', k, 'is about', guess)
    print('Newton-Raphson method took', counter, 'iterations to find the answer.')
    
def bisection_search():
    x = 24
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
        
    print('Square root of', x, 'is about', ans)
    print('Bisectional search method took', numGuesses, 'iterations to find the answer.')
   
print()
newton_raphson()
print()
bisection_search()
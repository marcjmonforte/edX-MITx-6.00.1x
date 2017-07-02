#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:52:56 2017

@author: mmonforte

Write a function called general_poly, that meets the specifications below. 
For example, general_poly([1, 2, 3, 4])(10) should evaluate to 1234 
because 1*(10**3) + 2*(10**2) + 3*(10**1) + 4*(10**0).

"""


def general_poly (L):
    """ L, a list of numbers (n0, n1, n2, ... nk)
    Returns a function, which when applied to a value x, returns the value 
    n0 * x^k + n1 * x^(k-1) + ... nk * x^0 """
    
    # Define function, which will be the return value of 'general_poly()'
    def inner_func(x):
        
        # Exponent set to length of L, minus one. Total is 0.
        e = (len(L) - 1)
        total = 0
        
        # Iterate through L.
        for item in L:
            
            # Establish foo value using formula, and add it to total. Decreate e counter by 1.
            foo = item * (x ** (e))
            total += foo
            e -= 1
        
        # Return the total, for this inner function.
        return total
    
    # Return the function, as requested by prompt.        
    return inner_func
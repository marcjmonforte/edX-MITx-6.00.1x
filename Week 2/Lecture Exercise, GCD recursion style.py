#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:18:01 2017

@author: mmonforte
"""

def gcdRecur(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    # Your code here
    
    if a == 0:
        return b
    elif b == 0:
        return a
    else:
        return gcdRecur(b, a%b)
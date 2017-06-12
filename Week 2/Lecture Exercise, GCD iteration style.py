#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:16:28 2017

@author: mmonforte
"""

def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    if a > b:
        gcd = a
    else:
        gcd = b
        
    while gcd != 1:
        if a % gcd == 0 and b % gcd == 0:
            return gcd
        else:
            gcd -= 1
    
    return gcd
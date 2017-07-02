#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 17:57:48 2017

@author: mmonforte

Write a function is_triangular that meets the specification below. 
A triangular number is a number obtained by the continued summation of integers 
starting from 1. For example, 1, 1+2, 1+2+3, 1+2+3+4, etc., corresponding to 
1, 3, 6, 10, etc., are triangular numbers.

"""

def is_triangular(k):
    """
    k, a positive integer
    returns True if k is triangular and False if not
    """
    # Triangle number formula : xn = n(n+1)/2.
    
    # Counters and empty list defined below.
    n = 1
    triangles = []
    
    # Establish first triangle number.
    triangle_number = (n * ( n + 1)) / 2
    
    # Keep calculating for next triangle number while k > triangle_number.
    while k >= triangle_number:
        
        # Add calculated triangle number to list.
        triangles.append(triangle_number)
        
        # Increase counter.
        n += 1
        
        # Re-evaluate triangle_number.
        triangle_number = (n * ( n + 1)) / 2
        
    # Once argument is not larger/equal to triangle_number, see if it's in the list.    
    return k in triangles
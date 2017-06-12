#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:05:20 2017

@author: mmonforte
"""

def polysum(n, s):
    """
    Input: 'n' is the number of sides; 's' is the length of the sides
    Output: returns the sum of the area and the square of the perimieter of the regulary polygon, to 4 decimal spaces
    """
    import math, decimal
    area = (0.25 * n * (s**2)) / math.tan(math.pi / n)
    perimeter = (n * s)
    
    return round(area + (perimeter**2), 4)
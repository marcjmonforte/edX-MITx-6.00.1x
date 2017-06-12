#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 11 23:18:21 2017

@author: mmonforte
"""

def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if len(aStr) <= 1:
        return char == aStr
    else:
        if aStr[len(aStr) // 2] == char:
            return True
        elif aStr[len(aStr) // 2] > char:
            return isIn(char, aStr[0:(len(aStr) // 2)])
        elif aStr[len(aStr) // 2] < char:
            return isIn(char, aStr[(len(aStr) // 2):])
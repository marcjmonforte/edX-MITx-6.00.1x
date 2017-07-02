#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:34:52 2017

@author: mmonforte

Write a function that satisfies the following docstring.

For example, if
largest_odd_times([2,2,4,4]) returns None
largest_odd_times([3,9,5,3,5,3]) returns 9

"""

def largest_odd_times(L):
    """ Assumes L is a non-empty list of ints
        Returns the largest element of L that occurs an odd number 
        of times in L. If no such element exists, returns None """
    
    # Establish a dictionary, to hold counters.
    dict = {}
    for i in L:
        if i in dict:
            dict[i] += 1
        else:
            dict[i] = 1
    
    #Establish an empty list, which will hold only the odd numbers.
    oddList = []
    
    # If the value of the key from 'dict' is odd, add that key to oddList.
    for item in dict:
        if dict[item] % 2 == 1:
            oddList.append(item)
    
    # If oddList is empty, return None.     
    if oddList == []:
        return None
    # Else, return the largest number from oddList.
    else:
        return max(oddList)
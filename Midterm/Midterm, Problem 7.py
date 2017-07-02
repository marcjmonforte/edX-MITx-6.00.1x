#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 19:19:39 2017

@author: mmonforte

Write a function called dict_invert that takes in a dictionary with immutable values 
and returns the inverse of the dictionary. The inverse of a dictionary d is another 
dictionary whose keys are the unique dictionary values in d. The value for a key in the 
inverse dictionary is a sorted list (increasing order) of all keys in d 
that have the same value in d.

Here are two examples:

If d = {1:10, 2:20, 3:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3]}
If d = {1:10, 2:20, 3:30, 4:30} then dict_invert(d) returns {10: [1], 20: [2], 30: [3, 4]}
If d = {4:True, 2:True, 0:True} then dict_invert(d) returns {True: [0, 2, 4]}

"""

def dict_invert(d):
    '''
    d: dict
    Returns an inverted dictionary according to the instructions above
    '''
    # Establish new dictionary.
    newDict = {}
    
    # Iterate through items in dictionary.
    for item in d:
        
        # If that value is already in newDict as a key, 
        # append the iterated key to the value, which should be a list.
        if d[item] in newDict:  
            newDict[d[item]].append(item)
            newDict[d[item]].sort()
            
        # If that value is not in newDict as a key,
        # create a new key using value as name, set it to a list, and append the key into the list.
        else:
            newKey = d[item]
            newDict[newKey] = []
            newDict[newKey].append(item)
            
    return newDict
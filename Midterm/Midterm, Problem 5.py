#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jul  1 18:28:21 2017

@author: mmonforte

Write a Python function that takes in a string and prints out a version of this string 
that does not contain any vowels, according to the specification below. 
Vowels are uppercase and lowercase 'a', 'e', 'i', 'o', 'u'.

For example, if s = "This is great!" then print_without_vowels will print Ths s grt!. 
If s = "a" then print_without_vowels will print the empty string .

"""

def print_without_vowels(s):
    '''
    s: the string to convert
    Finds a version of s without vowels and whose characters appear in the 
    same order they appear in s. Prints this version of s.
    Does not return anything
    '''
    
    # Establish vowels.
    vowels = ['a','e','i','o','u','A','E','I','O','U']
    
    # Establish temporary list.
    vowels_removed = []
    
    # Convert argument 's' into a iterable list.
    s_list = list(s)
    
    # Loop through each letter of list; consonants will be appended to temporary list.
    for letter in s_list:
        if letter not in vowels:
            vowels_removed.append(letter)
        
    # Join list together, and print it (not return, as per instructions.)    
    newString = ''.join(vowels_removed)
    print(newString)
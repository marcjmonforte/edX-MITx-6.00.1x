#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:21:27 2017

@author: mmonforte
"""

"""
Problem # 3
Assume s is a string of lower case characters.
Write a program that prints the longest substring of s in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', then your program should print
Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. For example, if s = 'abcbcd', then your program should print
Longest substring in alphabetical order is: abc
"""

s = 'czqriqfsqteavw'

longword = '' 
for x in range(len(s) - 1):
    for y in range(len(s) + 2):
        word = s[x:y]
        if word == ''.join(sorted(word)):
            if len(word) > len(longword):
                longword = word

print(longword)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun  6 20:21:18 2017

@author: mmonforte
"""

"""
Problem # 2
Assume s is a string of lower case characters.
Write a program that prints the number of times the string 'bob' occurs in s. 
For example, if s = 'azcbobobegghakl', then your program should print
Number of times bob occurs is: 2
"""

s = "azcbobobegghakl"

bobCount = 0

for num in range(len(s)):
    if s[num:num+3] == "bob":
        bobCount += 1
        
print("Number of times bob occurs is:", bobCount)
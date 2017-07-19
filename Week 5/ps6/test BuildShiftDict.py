#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 00:06:44 2017

@author: mmonforte
"""
 
lowerDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'j':9, 
            'i':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 
            'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 
            'z':26}
upperDict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'J':9, 
             'I':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 
             'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26, }
inv_lowerDict = {v: k for k, v in lowerDict.items()}
inv_upperDict = {v: k for k, v in upperDict.items()}
newLetterDict = {}
shift = 1

for letter in lowerDict:
    k = letter
    v_Value = lowerDict[letter] + shift
    
    while v_Value > 26:
        v_Value -= 26
    
    if v_Value in inv_lowerDict:
        v = inv_lowerDict[v_Value]
        
    newLetterDict[k] = v
    
for letter in upperDict:
    k = letter
    v_Value = upperDict[letter] + shift
    
    while v_Value > 26:
        v_Value -= 26
    
    if v_Value in inv_upperDict:
        v = inv_upperDict[v_Value]
        
    newLetterDict[k] = v
    
# print(newLetterDict)

message = 'test this, 123!'
newMessage = []

for letter in message:
    if letter in newLetterDict:
        newMessage.append(newLetterDict[letter])
    else:
        newMessage.append(letter)
        
print(''.join(newMessage))
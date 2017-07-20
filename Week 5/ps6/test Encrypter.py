#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 18 23:19:28 2017

@author: mmonforte
"""

lowerDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 
            'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 
            'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 
            'z':26}
upperDict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 
             'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 
             'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}

inv_lowerDict = {v: k for k, v in lowerDict.items()}
inv_upperDict = {v: k for k, v in upperDict.items()}

shift = int(input('Enter an integer: '))
oldMessage = input('Type anything: ')
newMessage = []

for letter in oldMessage:
    
    if (letter not in lowerDict) and (letter not in upperDict):
        newMessage.append(letter)
        
    
    elif letter == letter.lower():
        
        if letter in lowerDict:
            lowLetterValue = lowerDict[letter]
            newValue = lowLetterValue + shift
            while newValue > 26:
                newValue -= 26
            if newValue in inv_lowerDict:
                newMessage.append(inv_lowerDict[newValue])
                
    elif letter == letter.upper():
            
        if letter in upperDict:
            upLetterValue = upperDict[letter]
            newValue = upLetterValue + shift
            while newValue > 26:
                newValue -= 26
            if newValue in inv_upperDict:
                newMessage.append(inv_upperDict[newValue])
            
print(oldMessage)
print(''.join(newMessage))
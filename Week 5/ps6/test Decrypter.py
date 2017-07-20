#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 12:24:03 2017

@author: mmonforte
"""

#    def decrypt_message(self):
#        '''
#        Decrypt self.message_text by trying every possible shift value
#        and find the "best" one. We will define "best" as the shift that
#        creates the maximum number of real words when we use apply_shift(shift)
#        on the message text. If s is the original shift value used to encrypt
#        the message, then we would expect 26 - s to be the best shift value 
#        for decrypting it.
#
#        Note: if multiple shifts are equally good such that they all create 
#        the maximum number of you may choose any of those shifts (and their
#        corresponding decrypted messages) to return
#
#        Returns: a tuple of the best shift value used to decrypt the message
#        and the decrypted message text using that shift value
#        '''


lowerDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 
             'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 
             'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 
             'z':26}
upperDict = {'A':27, 'B':28, 'C':29, 'D':30, 'E':31, 'F':32, 'G':33, 'H':34, 'I':35, 
             'J':36, 'K':37, 'L':38, 'M':39, 'N':40, 'O':41, 'P':42, 'Q':43, 
             'R':44, 'S':45, 'T':46, 'U':47, 'V':48, 'W':49, 'X':50, 'Y':51, 'Z':52}
inv_lowerDict = {v: k for k, v in lowerDict.items()}
inv_upperDict = {v: k for k, v in upperDict.items()}
valid_words = ['test','poop','foobar','fooBar','spongebob', 'stay', 'woke'
               'strip', 'patience', 'veil', 'admission', 'new', 'nonsense']
testWord = 'Nonsense'

print('ORIGINALWORD: test =', list(testWord))
originalWordValues = []
for letter in testWord: # 'test' shifted by 2
    if letter in lowerDict:
        originalWordValues.append(lowerDict[letter])
    elif letter in upperDict:
        originalWordValues.append(upperDict[letter])
    else:
        originalWordValues.append(letter) 
print('ORIGINALWORDVALUES: ', originalWordValues, '\n')

shift = 1
while True:
    print('SHIFTCOUNT: ', shift)
    shiftedLetters = []        
    for value in originalWordValues:
        if value in inv_lowerDict:
            shiftedValue = value + shift
            while shiftedValue > 26:
                shiftedValue -= 26
            shiftedLetters.append(inv_lowerDict[shiftedValue])
            
        elif value in inv_upperDict:
            shiftedValue = value + shift
            while shiftedValue > 52:
                shiftedValue -= 26
            shiftedLetters.append(inv_upperDict[shiftedValue])
            
        else:
            shiftedLetters.append(value)
            
    shiftedWord = ''.join(shiftedLetters)
    print('SHIFTEDWORD: ',shiftedWord, "=", shiftedLetters)
    
    shiftedWordList = shiftedWord.split(' ')
    print('SHIFTEDWORDLIST: ', shiftedWordList, '\n')
    
    validation = 0
    for word in shiftedWordList:
        if word.lower() in valid_words:
            validation += 1
    if validation == len(shiftedWordList):
        break
    else:
        shift += 1
    
    if shift > 26:
            break

print('LOOP BROKEN.')        
print('SHIFT: ', shift)
print('SHIFTEDWORD: ', shiftedWord)
decrypted = (shift, shiftedWord)
print('FINAL RETURN TUPLE: ', decrypted)
        
        
        
        
        
        
        
        
        
        
        
        
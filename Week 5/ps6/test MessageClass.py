#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 19 00:51:43 2017

@author: mmonforte
"""

class Message(object):
    ### DO NOT MODIFY THIS METHOD ###
    def __init__(self, text):
        '''
        Initializes a Message object
                
        text (string): the message's text

        a Message object has two attributes:
            self.message_text (string, determined by input text)
            self.valid_words (list, determined using helper function load_words
        '''
        self.message_text = text
        #self.valid_words = load_words(WORDLIST_FILENAME)

    ### DO NOT MODIFY THIS METHOD ###
    def get_message_text(self):
        '''
        Used to safely access self.message_text outside of the class
        
        Returns: self.message_text
        '''
        return self.message_text

    ### DO NOT MODIFY THIS METHOD ###
    #def get_valid_words(self):
        '''
        Used to safely access a copy of self.valid_words outside of the class
        
        Returns: a COPY of self.valid_words
        '''
        #return self.valid_words[:]
        
    def build_shift_dict(self, shift):
        '''
        Creates a dictionary that can be used to apply a cipher to a letter.
        The dictionary maps every uppercase and lowercase letter to a
        character shifted down the alphabet by the input shift. The dictionary
        should have 52 keys of all the uppercase letters and all the lowercase
        letters only.        
        
        shift (integer): the amount by which to shift every letter of the 
        alphabet. 0 <= shift < 26

        Returns: a dictionary mapping a letter (string) to 
                 another letter (string). 
        '''
        lowerDict = {'a':1, 'b':2, 'c':3, 'd':4, 'e':5, 'f':6, 'g':7, 'h':8, 'i':9, 
                     'j':10, 'k':11, 'l':12, 'm':13, 'n':14, 'o':15, 'p':16, 'q':17, 
                     'r':18, 's':19, 't':20, 'u':21, 'v':22, 'w':23, 'x':24, 'y':25, 
                     'z':26}
        upperDict = {'A':1, 'B':2, 'C':3, 'D':4, 'E':5, 'F':6, 'G':7, 'H':8, 'I':9, 
                     'J':10, 'K':11, 'L':12, 'M':13, 'N':14, 'O':15, 'P':16, 'Q':17, 
                     'R':18, 'S':19, 'T':20, 'U':21, 'V':22, 'W':23, 'X':24, 'Y':25, 'Z':26}
        inv_lowerDict = {v: k for k, v in lowerDict.items()}
        inv_upperDict = {v: k for k, v in upperDict.items()}
        newLetterDict = {}
        
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
            
        return newLetterDict
        

    def apply_shift(self, shift):
        '''
        Applies the Caesar Cipher to self.message_text with the input shift.
        Creates a new string that is self.message_text shifted down the
        alphabet by some number of characters determined by the input shift        
        
        shift (integer): the shift with which to encrypt the message.
        0 <= shift < 26

        Returns: the message text (string) in which every character is shifted
             down the alphabet by the input shift
        '''
        
        newLetterDict = self.build_shift_dict(shift)
        newMessage = []
        for letter in self.message_text:
            if letter in newLetterDict:
                newMessage.append(newLetterDict[letter])
            else:
                newMessage.append(letter)
                
        return ''.join(newMessage)
    
test = Message('we are taking 6.00.1x')
print('INPUT: ', test.get_message_text())
print('EXPECTED: nv riv krbzex 6.00.1o')
print('ACTUAL: ', (test.apply_shift(17)))
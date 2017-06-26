#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 21:26:26 2017

@author: mmonforte

Next, implement the function getAvailableLetters that takes in one parameter - 
a list of letters, lettersGuessed. This function returns a string that is 
comprised of lowercase English letters - all lowercase English letters 
that are not in lettersGuessed.

Example Usage:
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getAvailableLetters(lettersGuessed))
abcdfghjlmnoqtuvwxyz

Note that this function should return the letters in alphabetical order, as in the example above.
For this function, you may assume that all the letters in lettersGuessed are lowercase.

"""

lettersGuessed = ['a', 'i', 'k', 'p', 'r', 's']

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    # Establish a list of letters in the alphabet.
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    alphabetList = list(alphabet)
    
    # For the letters in the lettersGuessed list...
    for letter in lettersGuessed:
        
        # If the letter is still in the alphabet, remove it.
        if letter in alphabetList:
            alphabetList.remove(letter)
    
    # Return a concatenated string of the remaining letters.            
    updatedAlphabet = ''.join(alphabetList)
    return updatedAlphabet
    
print(getAvailableLetters(lettersGuessed))
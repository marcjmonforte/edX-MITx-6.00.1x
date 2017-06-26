#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:18:42 2017

@author: mmonforte

We'll start by writing 3 simple functions that will help us easily code the Hangman problem. 
First, implement the function isWordGuessed that takes in two parameters - 
a string, secretWord, and a list of letters, lettersGuessed. This function returns a boolean - 
True if secretWord has been guessed (ie, all the letters of secretWord are in lettersGuessed) 
and False otherwise.

Example Usage:
>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(isWordGuessed(secretWord, lettersGuessed))
False

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

# Example parameters
secretWord = 'apple' 
lettersGuessed = ['e', 'a', 'p', 'k', 'l', 's']

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    
    # Create a list of letters from secretWord.
    secretWord_list = list(secretWord)
    
    # Iterate through each letter from lettersGuessed
    for letter in lettersGuessed:
        # If letter is in there...
        if letter in secretWord_list:
            # While it remains in there (i.e. multiple instances), keep removing it until none left.
            while letter in secretWord_list:
                secretWord_list.remove(letter)
    
    # Return True if all letters were removed.
    return secretWord_list == []

print(isWordGuessed(secretWord, lettersGuessed))
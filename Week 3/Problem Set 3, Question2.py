#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 20:49:04 2017

@author: mmonforte

Next, implement the function getGuessedWord that takes in two parameters - 
a string, secretWord, and a list of letters, lettersGuessed. 
This function returns a string that is comprised of letters and underscores, 
based on what letters in lettersGuessed are in secretWord. This shouldn't be 
too different from isWordGuessed!

Example Usage:

>>> secretWord = 'apple' 
>>> lettersGuessed = ['e', 'i', 'k', 'p', 'r', 's']
>>> print(getGuessedWord(secretWord, lettersGuessed))
'_ pp_ e'

For this function, you may assume that all the letters in secretWord and lettersGuessed are lowercase.
"""

# Example parameters
secretWord = 'apple' 
lettersGuessed = ['b', 'a', 'o', 'k', 'l', 's']

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
    what letters in secretWord have been guessed so far.
    '''
    
    # Create an empty list, which will hold your guesses.
    currentGuess_list = []
    
    # Index through each letter in secretWord, in order.
    for i in range(len(secretWord)):
        
        # If that letter is in the list of guessed letters...
        if secretWord[i] in lettersGuessed:
            
            # Add it to the current guesses list.
            currentGuess_list.append(secretWord[i] + ' ')
            
        else:
            # If not, add an underscore.
            currentGuess_list.append('_ ')
    
    # Concatenate all the items into a string.
    currentGuess = ''.join(currentGuess_list)
    
    return(currentGuess)
            
        
print(getGuessedWord(secretWord, lettersGuessed))
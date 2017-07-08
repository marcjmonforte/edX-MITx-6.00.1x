#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 22:45:25 2017

@author: mmonforte

The first step is to implement some code that allows us to calculate the score for a single word. 
The function getWordScore should accept as input a string of lowercase letters (a word) 
and return the integer score for that word, using the game's scoring rules.

Hints:
You may assume that the input word is always either a string of lowercase letters, or the empty string "".
You will want to use the SCRABBLE_LETTER_VALUES dictionary defined at the top of ps4a.py. 
You should not change its value.
Do not assume that there are always 7 letters in a hand! The parameter n is the number of letters 
required for a bonus score (the maximum number of letters in the hand). Our goal is to 
keep the code modular - if you want to try playing your word game with n=10 or n=4, 
you will be able to do it by simply changing the value of HAND_SIZE!

Testing: 
If this function is implemented properly, and you run test_ps4a.py, you should see that 
the test_getWordScore() tests pass. Also test your implementation of getWordScore, 
using some reasonable English words.
"""

def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # Need to import Scrabble Letter Values from ps4a.py
    import ps4a
    print("IMPORTING 'SCRABBLE_LETTER_VALUES': \n'", ps4a.SCRABBLE_LETTER_VALUES)
    print('')
    
    # Detects hand length from arg 'n'.
    print("HAND LENGTH:", n)
    print('')
    
    # Detects word length.
    wordLength = len(word)
    print("WORD LENGTH DETECTED:", wordLength)
    print('')
    wordValue = 0
    
    # Checks if letter in word is in dictionary from ps4a; increase word value, if so.
    for letter in word:
        if letter in ps4a.SCRABBLE_LETTER_VALUES.keys():
            print("LETTER DETECTED:", letter)
            wordValue += ps4a.SCRABBLE_LETTER_VALUES[letter]
            print("INCREASING WORDVALUE BY:", ps4a.SCRABBLE_LETTER_VALUES[letter])
            print("NEW WORDVALUE VALUE:", wordValue)
            print('')
    
    # Multiply word value by word length, as per Scrabble rules.
    wordValue = wordValue * wordLength
    print("WORDVALUE MULTIPLIED BY LENGTH (" + str(wordLength) + "):", wordValue)
    print('')
    
    # Add bonus points if all letters are used.
    if wordLength == n:
        wordValue += 50
        print("ADDITIONAL 50 POINTS ADDED FOR USING ALL LETTERS")
        print("BONUS WORD VALUE:", wordValue)
        print('')
    
    # Return word value.
    print("FINAL WORDVALUE:", wordValue)
    print('')
    return wordValue
    
# For testing purposes.
word = 'waybill'
n = 7
getWordScore(word, n)


word = 'a'
n = 1
getWordScore(word, n)


word = ''
n = 0
getWordScore(word, n)


word = 'water'
n = 7
getWordScore(word, n)


word = 'bbx'
n = 10
getWordScore(word, n)
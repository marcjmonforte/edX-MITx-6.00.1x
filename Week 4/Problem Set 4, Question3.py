#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 00:08:14 2017

@author: mmonforte

At this point, we have written code to generate a random hand and display that hand to the user. 
We can also ask the user for a word (Python's input) and score the word (using your getWordScore). 
However, at this point we have not written any code to verify that a word given by a player 
obeys the rules of the game. A valid word is in the word list; and it is composed entirely 
of letters from the current hand. Implement the isValidWord function.

Testing: Make sure the test_isValidWord tests pass. In addition, you will want to 
test your implementation by calling it multiple times on the same hand - 
what should the correct behavior be? Additionally, the empty string ('') is not a valid word - 
if you code this function correctly, you shouldn't need an additional check for this condition.
"""

def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # Establish coyp of hand, to avoid mutation.
    handCopy = hand.copy()
    
    # Continue through logic if word is in wordList; otherwise return False.
    if word in wordList:
        # Confirm that each letter exists in hand; if so, remove it.
        for letter in word:
            if letter in handCopy:
                # If the letter is in the hand but count zero from subtracting, return False.
                # i.e. not enough copies of same letter
                if handCopy[letter] == 0:
                    return False
                else:
                    handCopy[letter] -= 1  
            # If the letter isn't even in hand, return False.
            else:
                return False
    else:
        return False
    
    # Return True if all of the above works out.
    return True
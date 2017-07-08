#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 23:26:29 2017

@author: mmonforte

The player starts with a hand, a set of letters. As the player spells out words, 
letters from this set are used up. For example, the player could start out with the following hand: 
    a, q, l, m, u, i, l. The player could choose to spell the word quail . This would leave 
    the following letters in the player's hand: l, m. Your task is to implement the function updateHand, 
    which takes in two inputs - a hand and a word (string). updateHand uses letters from the hand 
    to spell the word, and then returns a copy of the hand, containing only the letters remaining. 
"""

def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # Establish copy of hand, to avoid mutation.
    hand = hand.copy()
    
    # Stating what the hand looks like to start.
    print("HAND, BEFORE REMOVING LETTERS:", hand)
    
    # Reducing value of letter key by 1 for each letter in word.
    for letter in word:
        print("CURRENT VALUE OF LETTER " + str(letter) + ":", hand[letter])
        hand[letter] -= 1
        print("UPDATED VALUE OF LETTER " + str(letter) + ":", hand[letter], "\n")
    
    # Stating what the hand looks like to finish.
    print("HAND, AFTER REMOVING LETTERS:", hand)
    
    # Return hand.
    return hand

# For testing purposes:    
hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
word = 'quail'
print(updateHand(hand, word))
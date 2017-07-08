#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jul  6 17:35:24 2017

@author: mmonforte

In ps4a.py, note that in the function playHand, there is a bunch of pseudocode. 
This pseudocode is provided to help guide you in writing your function. 
Check out the Why Pseudocode? resource to learn more about the What and Why of Pseudocode 
before you start coding your solution.

Note: Do not assume that there will always be 7 letters in a hand! 
The parameter n represents the size of the hand.

Testing: Case #1

Function Call:
    wordList = loadWords()
    playHand({'h':1, 'i':1, 'c':1, 'z':1, 'm':2, 'a':1}, wordList, 7)

Output:
  Current Hand:  a c i h m m z
  Enter word, or a "." to indicate that you are finished: him
  "him" earned 24 points. Total: 24 points
 
  Current Hand:  a c m z
  Enter word, or a "." to indicate that you are finished: cam
  "cam" earned 21 points. Total: 45 points
 
  Current Hand:  z
  Enter word, or a "." to indicate that you are finished: .
  Goodbye! Total score: 45 points. 
"""

def playHand(hand, wordList, n):
    """
    Allows the user to play the given hand, as follows:

    * The hand is displayed.
    * The user may input a word or a single period (the string ".") 
      to indicate they're done playing
    * Invalid words are rejected, and a message is displayed asking
      the user to choose another word until they enter a valid word or "."
    * When a valid word is entered, it uses up letters from the hand.
    * After every valid word: the score for that word is displayed,
      the remaining letters in the hand are displayed, and the user
      is asked to input another word.
    * The sum of the word scores is displayed when the hand finishes.
    * The hand finishes when there are no more unused letters or the user
      inputs a "."

      hand: dictionary (string -> int)
      wordList: list of lowercase strings
      n: integer (HAND_SIZE; i.e., hand size required for additional points)
      
    """

    # Constants / references (FOR TESTING)
#    SCRABBLE_LETTER_VALUES = {
#        'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10}  
#    hand = {'a': 1, 'p': 2, 'l': 1, 'e': 1}
#    wordList = ['tow', 'fast','eta','za','coffee']
    
    # Constants / references.  
    score = 0
    points = 0
    firstTry = True
    invalidGuess = False
    
    while True:
        # Take dictionary and make it printable.
        print("Current hand: ", end = "")
        for letter in hand:
            if hand[letter] > 0:
                print((letter + " ") * hand[letter], end = "")
            
        # Ask the player to make a guess.
        guess = input(str(('\nEnter word, or a "." to indicate that you are finished: ')))
        
         # Validate guess uses letters that player possesses.
        guessLetters = list(guess)
        for letters in guessLetters:
            if letters not in hand:
                invalidGuess = True
            
        # If guess is the dot, then exit loop and report score.
        if guess == ".":
            print("Goodbye! Total score: " + str(score) + "points\n")
            invalidGuess = False
            break
        
        elif invalidGuess == True:
            print("Invalid word, please try again.\n")
            invalidGuess = False
        
        # Elif the guess is an invalid word, then try again.
        elif guess not in wordList:
            print("Invalid word, please try again.\n")
        
        # Else (the word is valid), then take letters away and keep going.    
        else:
            
            # Now need to calculate score of word.
            for letter in guess:
                if letter in SCRABBLE_LETTER_VALUES:
                    points += SCRABBLE_LETTER_VALUES[letter]
            points = points * len(guess)
            
            # If first try, add 50 points.
            if firstTry == True:
                if len(guess) == sum(hand.values()):
                    points += 50
            score += points
    
            # Also need to reduce hand by letters used.
            for letter in guess:
                hand[letter] -= 1
            
            # Print result; reset points.
            print('" ' + guess + ' " earned ' + str(points) + ' points. Total: ' + str(score) + " points\n")
            points = 0
            firstTry = False
            
            # If hand is empty, exit and report score.
            letterInventory = 0
            for letter in hand:
                letterInventory += hand[letter]
                
            if letterInventory == 0:
                print("Run out of letters. Total score: " + str(score) + " points.\n")
                break
            else:
                continue
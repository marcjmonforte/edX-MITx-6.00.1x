#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun  8 18:36:23 2017

@author: mmonforte
"""

high = 100
low = 0
guess = (high + low) / 2
status = ""

print("Please think of a number between 0 and 100!")

while status != "c":
    print("Is your secret number", guess, "?")
    status = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")

    if status == "h".lower():
        high = guess
        guess = int((high + low) / 2)
        
    elif status == "l".lower():
        low = guess
        guess = int((high + low) / 2)
        
    elif status == "c".lower():
        break
    
    else:
        print("Try again.")
        continue
        
print("Game over. Your secret number was: ", guess)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jun 15 21:13:57 2017

@author: mmonforte

Now write a program that calculates the minimum fixed monthly payment needed 
in order pay off a credit card balance within 12 months. 
By a fixed monthly payment, we mean a single number which does not change each month, 
but instead is a constant amount that will be paid each month.

In this problem, we will not be dealing with a minimum monthly payment rate.

The following variables contain values as described below:
balance - the outstanding balance on the credit card
annualInterestRate - annual interest rate as a decimal

The program should print out one line: the lowest monthly payment 
that will pay off all debt in under 1 year, for example:
Lowest Payment: 180 

Assume that the interest is compounded monthly according to 
the balance at the end of the month (after the payment for that month is made). 
The monthly payment must be a multiple of $10 and is the same for all months. 
Notice that it is possible for the balance to become negative 
using this payment scheme, which is okay. A summary of the required math is found below:

Monthly interest rate = (Annual interest rate) / 12.0
Monthly unpaid balance = (Previous balance) - (Minimum fixed monthly payment)
Updated balance each month = (Monthly unpaid balance) + (Monthly interest rate x Monthly unpaid balance)

Test Case 1:
    balance = 3329
    annualInterestRate = 0.2

    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 310
  

Test Case 2:
    balance = 4773
    annualInterestRate = 0.2
	      
    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 440
  

Test Case 3:
    balance = 3926
    annualInterestRate = 0.2

    Result Your Code Should Generate:
    -------------------
    Lowest Payment: 360

"""
# Establish variables that we know / needed for the evaluation.
# Counter optional
balance = 3329
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate / 12
monthlyPayment = 0
updatedBalance = balance
counter = 0

# Will loop through everything until we find a rate that will reduce updatedBalance to 0.
while updatedBalance > 0:
    # Was stated that payments needed to happen in increments of $10
    monthlyPayment += 10
    # To reset balance back to actual balance when loop inevitably fails.
    updatedBalance = balance
    month = 1
    
    # For 12 months and while balance is not 0...
    while month <= 12 and updatedBalance > 0:
        # Subtract the ($10*n) amount
        updatedBalance -= monthlyPayment
        # Compound the interest AFTER making monthly payment
        interest = monthlyInterestRate * updatedBalance
        updatedBalance += interest
        # Increase month counter
        month += 1
        counter += 1
        
print("Lowest Payment: ", monthlyPayment)
print("Number of iterations: ", counter)
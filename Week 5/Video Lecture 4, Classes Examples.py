#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jul 11 22:07:46 2017

@author: mmonforte

Coding along with the lecture.
"""

class fraction(object):
    def __init__(self, numer, denom):
        self.numer = numer
        self.denom = denom
        
    def __str__(self):
        return str(self.numer) + ' / ' + str(self.denom)
    
    # "getter" functions are important for returning stored data
    def getNumer(self):
        return self.numer
    
    def getDenom(self):
        return self.denom
    
    # Need to redefine primitive "add" function since that won't work with these compound numbers.
    def __add__(self, other):
        numerNew = other.getDenom() * self.getNumer() + other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    
    def __sub__(self, other):
        numerNew = other.getDenom() * self.getNumer() - other.getNumer() * self.getDenom()
        denomNew = other.getDenom() * self.getDenom()
        return fraction(numerNew, denomNew)
    
    def convert(self):
        return self.getNumer() / self.getDenom()
    
oneHalf = fraction(1,2)
twoThirds = fraction(2,3)
threeQuarters = fraction(3,4)
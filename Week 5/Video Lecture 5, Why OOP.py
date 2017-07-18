#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:00:40 2017

@author: mmonforte
"""

class Animal(object):
    def __init__(self, age):
        self.age = age
        self.name = None
        
    def get_age(self):
        return self.age
    
    def get_name(self):
        return self.name
    
    def set_age(self, newage):
        self.age = newage
    
    def set_name(self, newname=""):
        self.name = newname
    
    def __str__(self):
        return "TYPE: animal, NAME: " + str(self.name) + ", AGE: " + str(self.age)
        
myanimal = Animal(3)
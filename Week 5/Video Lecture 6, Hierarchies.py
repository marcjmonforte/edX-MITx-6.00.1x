#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jul 12 22:08:41 2017

@author: mmonforte

HIERARCHY:
- Parent Class (superclass)
- Child Class (subclasses), which inherent data & behaviors from parent unless overwritten.
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
        return "Animal:" + str(self.name) + ":" + str(self.age)
    
class Cat(Animal):
    def speak(self):
        print("meow")
    
    def __str__(self):
        return "Cat:" + str(self.name) + ":" + str(self.age)
    
class Rabbit(Animal):
    def speak(self):
        print("meep")
        
    def __str__(self):
        return "Rabbit:" + str(self.name) + ":" + str(self.age)
    
class Person(Animal):
    def __init__(self, name, age):
        Animal.__init__(self, age)
        Animal.set_name(self, name)
        self.friends = []
        
    def get_friends(self):
        return self.friends

    def add_friend(self, fname):
        if fname not in self.friends:
            self.friends.append(fname)
            
    def speak(self):
        print("hello!")
        
    def age_diff(self, other):
        # alternate way = self.age - other.age
        diff = self.get_age() - other.get_age()
        if self.age > other.age:
            print(self.name, "is", diff, "years older than", other.name)
        else:
            print(self.name, "is", diff, "years younger than", other.name)
        
    def __str__(self):
        return "person:" + str(self.name) + ":" + str(self.age)

import random        
class Student(Person):
    def __init__(self, name, age, major = None):
        Person.__init__(self, name, age)
        self.major = major
        
    def change_major(self, newmajor):
        self.major = newmajor
        
    def speak(self):
        r= random.random()
        if r < 0.25:
            print("I have homework...")
        elif 0.25 <= r < 0.5:
            print('I need sleep...')
        elif 0.5 <= r < 0.75:
            print('I should eat...')
        else:
            print("I am watching TV!")
            
    def __str__(self):
        return "Student:" + str(self.name) + ":" + str(self.age) + ":" + str(self.major)
#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:00:27 2017

@author: mmonforte
"""

import datetime

class Person(object):
    d
    def __init__(self, name):
        """Create a person called 'name'."""
        self.name = name
        self.birthday = None
        self.lastName = name.split(' ')[-1]
    
    def getLastName(self):
        """Return self's last name."""
        return self.lastName
    
    def __str__(self):
        """Return self's full name."""
        return self.name
    
    def setBirthday(self, month, day, year):
        """Sets birthday to birthDate"""
        self.birthday = datetime.date(year, month, day)
        
    def getAge(self):
        """Return self's current age, in days."""
        if self.birthday == None:
            raise ValueError
        return (datetime.date.today() - self.birthday).days
    
    def __lt__(self, other):
        """Return True if self's name is lexicographically less than the other's name, and False otherwise."""
        if self.lastName == other.lastName:
            return self.name < other.name
        return self.lastName < other.lastName
    
p1 = Person('Mark Zuckerberg')
p1.setBirthday(5, 14, 84)

p2 = Person('Drew Houston')
p2.setBirthday(3, 4, 83)

p3 = Person('Bill Gates')
p3.setBirthday(10, 28, 55)

p4 = Person('Andrew Gates')

p5 = Person('Steve Wozniak')

personList = [p1, p2, p3, p4, p5]

print('List not yet sorted:')
print('-' * len('List not yet sorted:'))
for e in personList:
    print(e)
    
personList.sort()
print('\nList now sorted:')
print('-' * len('List now sorted:'))
for e in personList:
    print(e)
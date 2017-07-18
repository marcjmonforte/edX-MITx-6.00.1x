#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:11:39 2017

@author: mmonforte
"""

class Person(object):
    
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

class MITPerson(Person):
    nextIdNum = 0 # Next ID Number to assign.
    
    def __init__(self, name):
        Person.__init__(self, name) # Initialize Person attributes.
        self.idNum = MITPerson.nextIdNum # MITPerson attribute : unique ID.
        MITPerson.nextIdNum += 1
        
    def getIdNum(self):
        return self.idNum
    
    # Sorted MIT people uses their ID number, not name!
    def __lt__(self, other):
        return self.idNum < other.idNum
    
    def speak(self, utterance):
        return (self.getLastName() + " says: " + utterance) 
    
m3 = MITPerson('Mark Zuckerberg')
Person.setBirthday(m3, 5, 14, 84)
m2 = MITPerson('Drew Houston')
Person.setBirthday(m2, 3, 4, 83)
m1 = MITPerson('Bill Gates')
Person.setBirthday(m1, 10, 28, 55)
MITPersonList = [m1, m2, m3]

print('\nUnsorted:')
for e in MITPersonList:
    print(e)
    
MITPersonList.sort()
print('\nSorted:')
for e in MITPersonList:
    print(e) # Shows that they are sorted not alphabetically, but by ID.
    
p1 = MITPerson('Eric')
p2 = MITPerson('John')
p3 = MITPerson('John')
p4 = Person('John') # P4 is not an MITPerson, therefore does not have ID. How will it be sorted?

























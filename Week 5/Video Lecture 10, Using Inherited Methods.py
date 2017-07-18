#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 17 18:38:50 2017

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
    
class Student(MITPerson):
    pass    
    
class UG(Student):
    def __init__(self, name, classYear):
        MITPerson.__init__(self, name)
        self.year = classYear
        
    def getClass(self):
        return self.year
    
    def speak(self, utterance):
        return MITPerson.speak(self, "Dude, " + utterance)
    
class Grad(Student):
    pass

class TransferStudent(Student):
    pass

class Professor(MITPerson):
    def __init__(self, name, department):
        MITPerson.__init__(self, name)
        self.department = department
        
    def speak(self, utterance):
        new = 'In course ' + self.department + ', we say '
        return MITPerson.speak(self, new + utterance)
    
    def lecture(self, topic):
        return self.speak('It is obvious that ' + topic)

def isStudent(obj):
    return isinstance(obj, Student)

faculty = Professor('Doctor Arrogant', 'Six')


























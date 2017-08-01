class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """

        self.vals = {}
    
    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """

        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1
    
    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i)+":"+str(self.vals[i])+"\n"
        return s

class Bag(Container):
    
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """

        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """

        if e not in self.vals:
            return 0
        else:
            return self.vals[e]

    def __add__(self, other):
        """ assumes other is a Bag instance
            Returns dictionary of combined values between two Bag instances. """

        combinedBag = Bag()
        combinedBag.vals = self.vals.copy()
        for e in other.vals:
            for i in range(other.vals[e]):
                combinedBag.insert(e)
        return combinedBag

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        if e in self.vals:
            del self.vals[e]    
        else:
            None

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        return e in self.vals

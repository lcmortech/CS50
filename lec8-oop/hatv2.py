import random

class Hat:
	#def __init__(self):
	#class variables exist within the class itself and theres just 1 copy of that variable for all of the objects. they all share the same variable
		houses = ["Gryffiindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
		
		@classmethod
		
		
		
    def sort(cls, name): #cls becomes class by convention
		print(name, "is in", random.choice(self.houses))
        #print(name, "is in", "some house")

# common syntax for instantiating an instance of a certain class
hat = Hat()
hat.sort("Harry")

# we uses classes to represent some real world or fictional entity in code
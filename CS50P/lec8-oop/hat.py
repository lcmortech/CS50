import random

class Hat:
	def __init__(self):
		self.houses = ["Gryffiindor", "Hufflepuff", "Ravenclaw", "Slytherin"]
		
    def sort(self, name):
		print(name, "is in", random.choice(self.houses))
        #print(name, "is in", "some house")

# common syntax for instantiating an instance of a certain class
hat = Hat()
hat.sort("Harry")

# we uses classes to represent some real world or fictional entity in code
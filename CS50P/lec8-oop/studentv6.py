class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house
		
	def __str__(self):
		return f"{self.name} from {self.house}"
	
	# Getter - a function for a class that gets some attribute	
	#def house(self):
	@property #no colon needed!
		return self._house
	
	# Setter - a function in some class that sets some value	
	#def house(self, house):
	@house.setter #no colon needed!
	if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid Error - House not valid")
		self._house = house # the underscore is also what makes dictionaries so powerful
	# all of the error checking can be kept in the setter now, and will be called either when the object is created for the first time bc of init or if a programmer tries to circumvent that method
		
	def main():
		student = get_student()
		#student.house = "Number Four, Privet Drive" # can be used to circumvent/override conditional in class constructor
		print(student)
		
	def get_student():
		name = input("Name: ")
		house = input("House: ")
		
if __name__ = "__main__":
	main()

# introducing the @property and decorators
# properties - @property - an attribute that has even more defense mechanisms put into place and that you have more control over
# decorators functions that modify the behavior of other functions

# it will always be 1 argument for the getter (self), and 2 arguments for the setter
# not using the underscore in init ensures python recognizes the pattern and that error checking takes place
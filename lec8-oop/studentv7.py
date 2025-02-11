# important: python focuses on conventions, not hard constraints
# if an instance variable starts with an underscore or even a double underscore (private), please don't touch it
class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house
		
	def __str__(self):
		return f"{self.name} from {self.house}"
	
		
	@property #no colon needed!
		return self._house
	
		
	if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise ValueError("Invalid Error - House not valid")
			self._house = house # the underscore is also what makes 
		
	def main():
		student = get_student()
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
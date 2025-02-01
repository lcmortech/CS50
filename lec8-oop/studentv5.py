class Student:
	def __init__(self, name, house=None):
		if not name:
			raise MyCustomError("Missing name")
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise MyCustomError("Invalid house")
		self.name = name
		self.house = house
		

# def __str__(self) can be used to print out the description of an object instead of its default location
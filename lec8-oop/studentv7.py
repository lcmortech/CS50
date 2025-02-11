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
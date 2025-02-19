class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house
		
	def __str__(self):
		return f"{self.name} from {self.house}"
	
	# you can now call this method without creating an object first
	# now the get method is built into the class
	@classmethod	
	def get(cls):
		name = input("Name: ")
		house = input("House: ")
		return cls(name, house)
	
		
def main():
		#student = get_student() - bc of cls now becomes 
		student = Student.get()
		print(student)
		

		
# avoids accidentally executing main when creating a package or module	
if __name__ = "__main__":
	main()
	
	
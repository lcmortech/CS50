class Student:
	def __init__(self, name, house):
		self.name = name
		self.house = house
		
	def __str__(self):
		return f"{self.name} from {self.house}
		
	def main():
		student = get_student()
		student.house = "Privet Drive" # can be used to circumvent conditional in class constructor
		print(student)
		
	def get_student():
		name = input("Name: ")
		house = input("House: ")
		
if __name__ = "__main__":
	main()
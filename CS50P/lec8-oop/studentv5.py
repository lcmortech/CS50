class Student:
	def __init__(self, name, house=None, patronus):
		if not name:
			raise MyCustomError("Missing name")
		if house not in ["Gryffindor", "Hufflepuff", "Ravenclaw", "Slytherin"]:
			raise MyCustomError("Invalid house")
		self.name = name
		self.house = house
		self.patronus = patronus
# def __str__(self) - dunder str method. it can be used to print out the description of an object instead of its default location



	def __str__(self):
		print(f"{self.name} from {self.house}")
		
	def charm(self):
		match self.patronus:
			case "Stag":
				return "🦌"
			case "Jack Russell Terrier":
				return "🐶"
			case _:
				return "🪄"
		
	
	def get_student():
		name = input("Name": )
		house = input("House": )
		patronus = input("Patronus": )
		
		return Sudent(name, house, patronus)
		
	def main():
		 student = get_student()
		 print("Expecto Patronum")
		 print(student.charm())
		 
		 

if __name__ == "__main__":
	main()
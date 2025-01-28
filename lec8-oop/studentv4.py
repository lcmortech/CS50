# CLASSES - classes allow you to invent your own datatype (or object - OOP) and give them a name
# import sys (not recommended)
# 1 - You can define your own class (datatype)
class Student: # constructor - acts as a bllueprint
	def __init__(self, name, house): # dunder/instance method. implements the initialization of an object in python
		if not name:
			#sys.exit("Missing name")- not rec
			# it is better to raise your own exceptions instead
		self.name = name
		self.house = house

# 3 - You can access those same sttributes using code like this
def main():
	student = get_student()
	print(f"{student.name} from {student.house}")
	
	
# classes have "attributes": properties of sorts that allow to specify values inside of them. The syntax is "."
# 2 - You can store "attributes" inside of it using dot notation
# These attributes are really called properties/instance variables
def get_student():
	name = input("Name: ")
	house = input("House: ")
	student = Student(name, house)
	#student == Student() # creating an object of class Student
	#student.name = input("Name: ")
	#student.house = input("House: ")
	return student
	
if __name__ == "__main__":
	main()

# CLASSES - classes allow you to invent your own datatype (or object - OOP) and give them a name

# 1 - You can define your own class (datatype)
class Student:
	def __init__(self): # dunder/instance method

# 3 - You can access those same sttributes using code like this
def main():
	student = get_student()
	print(f"{student.name} from {student.house}")
	
	
# classes have "attributes": properties of sorts that allow to specify values inside of them. The syntax is "."
# 2 - You can store "attributes" inside of it using dot notation
# These attributes are really called properties/instance variables
def get_student():
	student == Student() # creating an object of class Student
	student.name = input("Name: ")
	student.house = input("House: ")
	return student
	
if __name__ == "__main__":
	main()

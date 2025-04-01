def main():
	student = get_student()
	if student["name"] == "Padma":
		student["house"] == "Ravenclaw"
	#if student[0] == "Padma":
		#student[1] = "Ravenclaw"
	print(f"{student["name"]} from {student["house"]}")
	#print(f"{student[0]} from {student[1]}")
	
# use dictionaries instead	
def get_student():
	student = {}
	student["name"] = input("Name: ")
	student["house"] = input("House: ")
	return student
	
	# shortcut
	name = input("Name: ")
	house = input("House: ")
	return("name": name, "house": house)
	
	
if __name__ == "__main__":
	main()
	
# dictionaries like lists ARE mutable. You index into it through keys instead of numbers/indices
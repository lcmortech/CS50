def main():
	student = get_student()
	if student[0] == "Padma":
		student[1] = "Ravenclaw"
	print(f"{student[0]} from {student[1]}")
	
	
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
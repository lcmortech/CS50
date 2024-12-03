names = []

# # for _ in range(3):
# #     name = input("What's your name?" )
# #     names.append[name]
# # # print(f"hello, {name}")
# # v2
# for _ in range(3):
# 	names.append(input("What's your name?" ))

# for name in sorted(names):
# 	print(f"hello", {name})
# # made shorter

# OPEN keyword - allows you to specify what you want to read from or write to

# names = input("What's your name? ")

# file = open("names.txt", "w") # creates file and allows you to write to it
# file.write(f"{name}\n")
# file.close()

# by changing the "w" to "a", the file goes from rewritable to editable (append)

# instead of using file.close(), we can use the with keyword instead

# names = input("What's your name? ")

# with open("names.txt", "r") as file:
# file.write(f"{name}\n")
# file.close()

# w, a, r (write, append/edit, read)
# with open("names.txt", "r") as file:
# 	lines = file.readlines()
	
# for line in lines:
# 	print("hello,", line.strip())

# with open("names.txt") as file:
# 	for line in file:
# 		names.append(line.lstrip())
		
# for name in sorted(names):
# 	print(f"hello, {name}")
	
# sorted shorter
# with open("names.txt") as file:
# 	for line in sorted(file):
# 		print("hello", line.rstrip())
		
# # sorted(iterable, /, *, key=None, reverse=False)
# # reverses sort order of names		
# for name in sorted(names, reverse=True):
# 	print(f"hello, {name"})
		

# use conditionals to find a name in open file using "r"

# storing a name and house using a csv file
with open("names.csv") as file:
	for line in file:
		name, house = line.rstrip().split(",")
		student = {}
		student ["name"] = name
		student ["house"] = house
		students.append(student)
		# print(f"{row[0]} is in {row[1]}")
# 		students.append(f"{name} is in {house}")

def get_name(student):
	return student["name"]
	
def get_house(student):
	return student["house"]
		
for student in sorted(students, key=lambda student: student["name"] reverse= True):
 	print(f"{student['name']} is in {student['house']}")

# break night - friendsgiving 2024

# Why does line 5 break?
# The address "Number Four, Private Drive" has a comma in it

# There's a CSV module that's useful for such corner cases, like the funciton csv.reader
with open("students.csv") as file:
	reader = csv.DictReader(file)
	# reader = csv.reader(file)
	for name, home in reader:
		students.append({"name": name, "home": home})
		#students.append({"name" : row[0], "home": row[1]})

# you don't have to rely on a row as a list or unpack things manually
# we could store the names of the columns in the csv file itself
# use dictionary (csv.DictReader) reader instead of csv reader

# ====
# thanksgiving break 2024
# thanksgiving day 2024
# movie night 2024
# ===


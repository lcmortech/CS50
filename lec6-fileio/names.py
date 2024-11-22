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
		
for student in sorted(students):
 	print(f"{student['name']} is in {student['house']}")


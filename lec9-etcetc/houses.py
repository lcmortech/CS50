students = [
	{"name": "Hermoine", "house": "Gryffindor"},
	{"name": "Harry", "house": "Gryffindor"},
	{"name": "Ron", "house": "Gryffindor"},
	{"name": "Draco", "house": "Slytherin"},
	{"name": "Padma", "house": "Ravenclaw"}
]

#houses = []
houses = set() # dupes are auto eliminated
for student in students:
	if student["house"] not in houses:
		houses.add(student["house"]) #its add not append for sets
		#houses.append(student["house"])
		
for house in sorted(houses):
	print(house)
#dictionary comprehensions

students = ["Hermoine", "Harry", "Ron"]

gryffindors = []

for student in students:
	gryffindors.append({"name": student,"house": "Gryffindor"})
	
#rebuilding the prev dictionary
print(gryffindors)
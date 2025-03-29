#dictionary comprehensions

students = ["Hermoine", "Harry", "Ron"]

#gryffindors = []

#for student in students:
#	gryffindors.append({"name": student,"house": "Gryffindor"})

# list comprehension ex
gryffindors = [{"name": student, "house": "Gryffindor"} for student in students] # from the list of students

# dictionary comprehension ex
gryffindors = {student: "Gryffindor" for student in students}

ranks = [1,2,3]

ranked_students = {rank: student for rank, student in zip(ranks, students)} # holy smokes I did it with zip! (I'm sure he meant enumerate tho)

# Malan ex

	
#rebuilding the prev dictionary
print(gryffindors)
print(ranked_students)
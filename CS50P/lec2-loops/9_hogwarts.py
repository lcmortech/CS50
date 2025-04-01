# using lists with for loops
'''
students = ["Hermoine", "Harry", "Ron"]

print(students[0])
print(students[1])
print(students[2])
print(students[3])

for student in students:
    print(students[student])
'''
'''
students = ["Hermoine", "Harry", "Ron", "Draco"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]
'''
'''
students = {
"Hermoine":"Gryffindor", 
"Harry": "Gryffindor"},
"Ron": "Gryffindor",
"Draco": "Slytherin"
}
'''
'''

print(students["Hermoine"])
print(students["Harry"])
print(students["Ron"])
print(students["Draco"])
'''
# when you use a for loop over a dict, it only returns the kes by default:
# print(student) 
'''
for student in students:
    print(students[student])


for student in students:
    print(student, students[student])
'''

# there are three keys in the following dictionary:
students = [
    {"name": "Hermoine", "house": "Gryffindor", "patronus": "Otter"},
    {"name": "Harry", "house": "Gryffindor", "patronus": "Stag"},
    {"name": "Ron", "house": "Gryffindor", "patronus": "Jack Russell Terrier"}, 
    {"name": "Draco", "house": "Slytherin", "patronus": None}
]

for student in students:
    print(student["name"], student["house"], student["patronus", sep=", "])
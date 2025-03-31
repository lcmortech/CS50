students = ["Hermoine", "Harry", "Ron"]

for i in range(len(students)):
    print(i + 1, students[i])

# enumerate - enumerate(iterable, start=0) - you can get both the key and item

for i, student in enumerate(students):
    print(i + 1, student)
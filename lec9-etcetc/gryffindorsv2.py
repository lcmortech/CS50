# list comprehensions

students = {"name": "Hermoine", "house": "Gryffindor"},
{"name": "Harry", "house": "Gryffindor"}, {"name": "Ron", "house": "Gryffindor"}, {"name": "Draco", "house": "Slytherin"}



#for gryffindor in gryffindors:
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
   print(gryffindor["name"])
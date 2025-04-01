# list comprehensions

students = {"name": "Hermoine", "house": "Gryffindor"},
{"name": "Harry", "house": "Gryffindor"}, {"name": "Ron", "house": "Gryffindor"}, {"name": "Draco", "house": "Slytherin"}

# gryffindors = [student["name"] for student in students #if student["house"] == "Gryffindor"]

# for gryffindor in sorted(gryffindors):
#   print(gryffindor)

#def is_gryffindor(s):
#   return s["house"] == "Gryffindor"
   # return True - not necessary
   #else: - no need to
   #   return False - explicitly return boolean

# or conditional inclusion/exclusion - use filter for bool
gryffindors = filter(lambda s: s["house"] == "Gryffindor", students) # you want filter to call the function for you

#for gryffindor in gryffindors:
for gryffindor in sorted(gryffindors, key=lambda s: s["name"]):
   print(gryffindor["name"])
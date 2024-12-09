import csv

name = input("What is your name?")
home = input("Where is your home?")

# with open("students.csv", "a") as file:
   # writer = csv.writer(file)
   # writer.writerow([name, home])

# another way to implement this is using a dictionary (DictWriter)
with open("students.csv", "a") as file:
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})

# PIL - pillow.readthedocs.io - allows you to navigate image files as well and to perform operations on image files, and even animate them
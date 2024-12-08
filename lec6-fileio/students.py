import csv

name = input("What is your name?")
home = input("Where is your home?")

with open("students.csv", "a") as file:
    writer = csv.writer(file)
    writer.writerow([name, home])

# another way to implement this is using a dictionary (DictWriter)
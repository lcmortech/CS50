# type hints - use pip install mypy to check if our variables are the correct type 

def meow(num):
	for _ in range(num):
		print("meow")

#number: int = input("Number: ") must change type
number: int = int(input("Number: "))
meow(num)

# when a function in python does not explicitly return a value, its implicit return value is none
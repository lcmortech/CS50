def meow(n: int) -> str:
	"""Meow n times. (doctstring format)"""
	return "meow\n" * n
	
	
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="") #fixing bug that comes with backslash n


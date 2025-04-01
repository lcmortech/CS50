def meow(n: int) -> str:
	"""
	Meow n times. (doctstring format)
	:param n: Number of times to meow
	:type n: int
	:raise TypeErrorr: If n is not an int
	:return: A string of n meows, one per line
	:rtype: str (restructured text, markdown type language) - not specific to python, helps w printing and other tasks
	"""
	return "meow\n" * n
	
	
number: int = int(input("Number: "))
meows: str = meow(number)
print(meows, end="") #fixing bug that comes with backslash n


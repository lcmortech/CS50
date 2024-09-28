# this is the basis of solving the fizzbuzz problem:

'''
x = int(input(" What's x? "))

if x % 2 == 0:
    print("Even")
else:
    print("Odd")
'''

def main():
	x = int(input("What is x? "))
	
	if is_even(x):
		print("Even")
	else:
		print("Odd")
	
# introducing the bool type: True, False (only 2 options)

'''
def is_even(num):
	if num % 2 == 0:
		return True
	else:
		return False
'''

# more pythonic:
'''
def is_even:
    return True if num % 2 == 0 else return False
'''

# even more pythonic:
# what happens in paranthesis happens FIRST
'''
def is_even(num):
    return (num % 2 == 0)
'''
# * paranthesis not necessary in this case due to order of operations

# most pythonic

def is_even(num):
    return num % 2 == 0


main()

# Note: if you write a function that returns a string, you can use the built-in string functions on it
		


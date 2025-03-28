'''
try:
    x = int(input("What's x? "))
    print(f"x is {x}")

except ValueError:
    print("Please input a number")

# problem with NameError (due to the order of operations)
else:
    print(f"x is {x}")
# the user might input a string (value error)
# it's good to be specific with the error instead of leaving "except" as is
'''

def main():
    x = get_int()
    print(f"x is {x}")

def get_int():
	while True:
    	try:
        	x = int(input("What's x? "))
        	break # instead of else: break
    	except ValueError:
        	print("x is not an integer")
 		#else:
        	#break
print(f"x is {x}")

# abstracted away getting an integer
# It's up to you to add a prompt for the user to see when asked for input
def main():
    x = get_int("What's x? ")
    print(f"x is {x}")

def get_int(prompt):
	while True:
		try:
			return int(input(prompt))
		except ValueError:
			pass
			#print("x is not an integer")

# the raise keyword is briefly mentioned


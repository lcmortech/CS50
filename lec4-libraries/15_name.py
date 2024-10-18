import sys

# # if you attempt to print a full name
# # Check for errors
# if len(sys.argv) < 2:
#     print("Too few arguments")
# elif len(sys.argv) > 2:
# 	sys.exit("Too many arguments")

# # printing name tags while not checking for arguments
# 	print("Hello, my name is", sys.argv[1])

# # prints first name given in command line
# # >> "Hello, my name is Name"

if len(sys.argv) < 2:
	sys.exit("Too few arguments")
for arg in sys.argv[1:]:
	#[1:-1]:
	print("Hello,my nameis", arg)
	
	# using a negative number starts the counting in the other direction
	
	# PACKAGES
	# PyPI pypi.org - python package index (similar to npm in js)
	# pypi.org/project/cowsay
	# pip - python
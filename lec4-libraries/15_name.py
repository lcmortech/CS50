import sys

# if you attempt to print a full name
# Check for errors
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
	print("Too many arguments")

# printing name tags while not checking for arguments
	print("Hello, my name is", sys.argv[1])

# prints first name given in command line
# >> "Hello, my name is Name"
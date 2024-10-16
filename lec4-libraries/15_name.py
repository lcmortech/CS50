import sys

# if you attempt to print a full name
if len(sys.argv) < 2:
    print("Too few arguments")
elif len(sys.argv) > 2:
	print("Too many arguments")
else:
	print("Hello, my name is", sys.argv[1])

# prints first name given in command line
# >> "Hello, my name is Name"
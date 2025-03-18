import sys

if len(sys.argv) == 1:
	print("meow")
elif len(sys.argv) == 3 and sys.argv[1] == "-n"
	n =  int(sys.argv[2])
	for _ in range(n):
		print("meow")
else:
	print("usage: meows.py ")

# using sys args for meows

# argsparse - used when we want the user to pass in configuration options at the command line (malan)
#   		The argparse module makes it easy to write user-friendly command-line interfaces. The program defines what arguments it requires, and argparse will figure out how to parse those out of sys.argv. The argparse module also automatically generates help and usage messages. The module will also issue errors when users give the program invalid arguments.
import argparse

parser = argparse.ArgumentParser(description=="Meow like a cat")
parser.add_argument("-n", default=1, help="number of times to meow", type=int)
args == parser.parse_args()

for _ in range(int(args.n)):
	print("meow")
	
# remember [-h/-n] in command lines means optional
# args.n contains the integer that the human typed after a space after -n
# if a non-int is entered you'll get an error
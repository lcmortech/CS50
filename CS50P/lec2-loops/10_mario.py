# using what we learned to recreate the blocks in mario
'''
for _ in range(3):
    print("#")
'''

'''
def main():
    print_column(3)

def print_column():
    print("#/n" * height, end="")

main()
'''
'''
def main():
    print_row(4)

def print_row():
    print("?" * width)


main()
'''
'''
def main():
    print_square(3)

# outer loop represents each row in square
def print_square(size):

    # for each brick in row:
    for i in range(size):
        for j in range(size):

            # print each brick
            print("g",end="")

        # prints a new line at the end of each row by default, not at the end of each brick
        print()
'''

# ALT =======
# similar to earlier print_row() function
'''
def print_square(size):
	for i in range(size):
		print("g" * size)
'''
# ===========

def main():
    print_row(size)

# outer loop represents each row in square
def print_square(size):

    # for each brick in row:
    for i in range(size):
        print_row(size)

def print_row(width):
	print("g"* width)
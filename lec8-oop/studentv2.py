
def main():
	student = get_student()
    # name, house = get_name() # abstraction
    house = get_house()
    print(f"{name [0]} from {house [1]}") # gets first and second item in tuple

def get_student(self):
        name = input("Name: ")
		house = input("House: ")
		return (name, house) # more explicit tuple
		#return name, house # this returns a tuple under the hood
    
def get_house():
        return input("House: ")

if__name__ == "__main__":
    main()

	# - tuple - immutable list. good for defense coding, better than lists

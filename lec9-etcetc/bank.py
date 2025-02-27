# global - makes a local variable global in scope
# local - exists within the context of a function

balance = 0 # variable is out of scope for defs

def main():
	print("Balance:", balance)
	deposit(100)
	withdraw(50)
	print("Balance:", balance)
	
	
def deposit(n):
	 global balance
	 balance += n
	
	
def withdraw(n):
	global balance
	balance -= n
	
if __name__ == "__main__": #calls main function if file name is "main"
    main()
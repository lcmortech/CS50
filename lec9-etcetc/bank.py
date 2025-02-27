# global - makes a local variable global in scope

balance = 0

def main():
	print("Balance:", balance)
	deposit(100)
	withdraw(50)
	print("Balance:", balance)
	
	
def deposit(n):
	balance += n
	
	
def withdraw(n):
	balance -= n
	
if __name__ == "__main__": #calls main function if file name is "main"
    main()
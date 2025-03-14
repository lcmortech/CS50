# OOP

class Account:
	def __init__(self):
		self._balance = 0 # ._ convention for privacy
		

	@property
	def balance(self):
		return self._balance
		
	def deposit(self, n):
		self._balance += n #appending n amount to curr balance
		
	def withdraw(self, n):
		sel._balance -= n #subtracting n amount from curr balance
		
	def main():
		account = Account() #create new account object
		print("Balance:", account.balance)
		account.deposit(100)
		account.withdraw(50)
		print("Balance:", account.balance)
		
if __name__ == "__main__":
	main()
	
# globals are meant to be used sparingly bc things can get messy quickly

# constants - variables that are immutable and cannot be changed. good for defensive programming, but is only a convention in python
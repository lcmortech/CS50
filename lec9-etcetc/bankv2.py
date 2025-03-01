# OOP

class Account:
	def __init__(self):
		self._balance = 0 # ._ convention for privacy
		

	@property
	def balance(self):
		return self._balance
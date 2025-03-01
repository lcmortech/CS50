# OOP

class Account:
	def __init__(self):
		self._balance = 0
		

	@property
	def balance(self):
		return self._balance
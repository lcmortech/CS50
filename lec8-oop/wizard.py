class Wizard: # the superclass
	def __init__(self, name):
		if not name:
			raise.ValueError("Missing Name")
		self.name = name
		

class Student(Wizard): # subclass of wizard
	def __init__(self, name, house): # acts like a constructor
		super().__init__(name) # accesses the superclass
		#self.name = name - is already in Wizard class
		self.house = house
		
		
class Professor(Wizard): # subclass of wizard
	def __init__(self, name, subject): # acts like a constructor
		super().__init__(name) # access the superclass		
		self.subject = subject
		#self.name = name - is already in Wizard class
		
		
# docs.python.org3/library/exceptions.html
# operator overloading - plus does not have to equal addition, and minus does not have to mean subtraction
		
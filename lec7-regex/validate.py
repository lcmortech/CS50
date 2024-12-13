# make sure to always strip input string
email = input("What is your email? ").strip()

# define two variables at once
# if username is valid print valid, else print invalid
username, domain = email.split()

# checking username isn't empty
# checking if both username and . in domain
if username and "." in domain:
	print("Valid!")
else:
	print("Invalid!")
	
# let's be more specific
	
	

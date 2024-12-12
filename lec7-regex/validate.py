# make sure to always strip input string
email = input("What is your email? ").strip()

# define two variables at once
# if username is valid print valid, else print invalid
username, domain = email.split()

if username:
	print("Valid!")
else:
	print("Invalid!")

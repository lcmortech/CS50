import re

# make sure to always strip input string
email = input("What is your email? ").strip()

# define two variables at once
# if username is valid print valid, else print invalid
username, domain = email.split()

# checking username isn't empty
# checking if both username and . in domain
#if username and "." in domain:
#	
# let's be more specific
# closer but can still be bypassed easily, ex pass@.edu is valid
#if username and domain.endswith(".edu"):
# no better than prev version but still using the re library now
#if re.search("@", email): 
# add chars:
if re.search(".*@.*", email)
	print("Valid!")
else:
	print("Invalid!")

# intro to re library
# most useful function is re.search(pattern, string, flags=0)
# pattern - a pattern that you want to search for (str from a user)
# string - the actual string being searched for
# flags - we won't use this, we'll just pass through a few arguments instead

# regex chars introduced: 
# . 
# * 
# + 
# ? 
# {m} 
# {m,n}


	
	

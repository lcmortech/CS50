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
# email is the variable being searched
#if re.search("@", email): 
# add chars:
# if re.search(".*@.*", email)
# changed dot star to dot plus to require repeitions
# alt "..*@..*"
# it uses a finite state machine (a non-deterministic finite automaton) under the hood
# Valid, but not as precise
# if re.search(r"^.+@.+\.edu$", email): # ^ start, added / (escape char)for period, $ end
if re.search(r"^[^@]+@[^@]+\.edu$", email):
	print("Valid!")
else:
	print("Invalid!")

# intro to re library
# most useful function is re.search(pattern, string, flags=0)
# pattern - a pattern that you want to search for (str from a user)
# string - the actual string being searched for
# flags - we won't use this, we'll just pass through a few arguments instead

# regex chars introduced (re.search()): 
# . - allows any char except a newline
# * - 0 or more repetions
# + - 1 or more repetitions
# ? - 0 or more repetitions
# {m} - m (variable) number of repetitions
# {m,n} - m-n (variable) range or repetitions 

# google forms and vs code also contains a regex feature

# ^ - matches the start of the string
# $ matches the end of the string and just before the newline at the end of the string

# [] set of characters
# [^] complementing the set
# (review) a set of curly braces can be used to specify a number of characters
# [a - z] means a through z (range)

# ====christmas eve====
# ====christmas========
	

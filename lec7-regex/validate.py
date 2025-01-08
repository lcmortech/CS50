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
# this is still the easiest method:
# if re.search(r".@+@.+", email)
# if re.search(r"^[a-zA-Z0-9_]+@[^@]+\.edu$", email):
# you can also write email.lower()
# if re.search(r"^\w+@\w+\.edu$", email):
# ignore the case of the input wo changing its value
# if re.search(r"^\w+\w+\.edu$", email, re.IGNORECASE):
# allow for sub-domains                  
# if re.search(r"^[a-zA-Z0-9_.]\w+@(\w+\.)?\w+\.edu$",email,re.IGNORECASE):
# alt code to prev (neither way is better, depends on design)
if re.search(r"^[a-zA-Z0-0-9_\.])?\w+\.edu$",email,re.IGNORECASE):
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
# + - 1 or more repetitions of the thing to the left
# ? - 0 or more repetitions
# {m} - m (variable) specific number of repetitions
# {m,n} - m-n (variable) range or repetitions 

# google forms and vs code also contains a regex feature

# ^ - match from the start of the string
# $ matches the end of the string and just before the newline at the end of the string

# [] set of characters
# [^] complementing the set. must be INSIDE the brackets and precede the set of characters to work this way
# (review) a set of curly braces can be used to specify a number of characters
# [a - z] means a through z (range), or [a-zA-Z0-9_] for all characters

# ====christmas eve====
# ====christmas========
	
# SHORTCUT CHARS
# \d decimal digit
# \D NOT a decimal digit
# \s whitespace characters
# \S NOT a whitespace character
# \w word character...as well as numbers and the underscore
# \W NOT a word character

# re.search built in variables/constants
# re.IGNORECASE - ignores the case of the input without changing its value
# re.MULTILINE
# re.DOTALL

# NEW YEARS DAY BREAK

# break
# break 2

re.match(pattern, string, flags = 0)
re.fullmatch(pattern, string, flags = 0) # replaces carrot or dollar sign

name = input("What's your name? ").strip()
print(f"hello, {name}")


# Sorting hat style program
# learning the python built-in match feature

name = input("What's your name? ")

'''
if name == "Harry":
    print("Gryffindor")
elif name == "Hermoine":
    print("Gryffindor")
elif name == "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
                            
'''

# clean up using or conditional
'''
if name == "Harry" or "Hermoine" or "Ron":
    print("Gryffindor")
elif name == "Draco":
    print("Slytherin")
else:
    print("Who?")
'''
# using the match case feature:

'''
match name:
	case "Harry":
		print("Gryffindor")
	case "Hermoine":
		print("Gryffindor")
	case "Ron":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")
'''

# further tighteningo it up, no need for "break" or "default" like in traditional switch case statement, just the undescore at the end
match name:
	case "Harry"| "Hermoine"| "Ron":
		print("Gryffindor")
	case "Draco":
		print("Slytherin")
	case _:
		print("Who?")
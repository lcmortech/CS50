# unpacking

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

#coins = [100, 50, 25]
coins = {"galleons": 100, "sickles": 50, "knuts": 25}


#print(total(100, 50, 25), "Knuts")

#Using * (unpacking operator) to unpack coins instead
# allows us to take a data structure and pass it in individually. works for tuples not sets. its the equivalent of a comma separated list. number of arguments must match
#print(total(*coins), "Knuts")
# print(total(galleons=100, sickles=50, knuts=25), "Knuts")

# unpack a dict with ** instead, unpacks named arguments
# you can still add default arguments but they're not necessary
print(total(**coins), "Knuts")

# with *args (asterisk arguments) and **kwargs (keyword arguments) a function's parameters can become variadic - take a variable number of arguments
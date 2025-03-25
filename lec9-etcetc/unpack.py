# unpacking

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

#print(total(100, 50, 25), "Knuts")

#Using * (unpacking operator) to unpack coins instead
# allows us to take a data structure and pass it in individually. works for tuples not sets. its the equivalent of a comma separated list
print(total(*coins), "Knuts")

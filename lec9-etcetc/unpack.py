# unpacking

def total(galleons, sickles, knuts):
    return(galleons * 17 + sickles) * 29 + knuts

coins = [100, 50, 25]

#print(total(100, 50, 25), "Knuts")

#Using * (unpacking operator) to unpack coins instead
print(total(*coins), "Knuts")
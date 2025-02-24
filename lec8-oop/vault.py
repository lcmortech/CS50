class Vault
    def __init__(self, galleons, sickles=0, knuts=0):
        self.galleons = galleons
        self.sickles = sickles
        self.knuts = knuts

        def __str__(self):
            return f"{self.galleons} Galleons, {self.sickles} Sickles, {self.knuts} Knuts"

        # in operater overloading, whatever the operand is on the left and right will become self and other, respectively
        def __add__(self, other): # sticking with convention
			galleons = potter.galleons + weasley.galleons
            sickles = potter.sickles + weasley.sickles
            knuts = potter.knuts + weasley.knuts
			# add a brand new bigger vault
			return Vault(galleons, sickles, knuts) # teaches python how to add two vaults together


potter = Vault(100, 50, 25)
print(potter)

weasley = Valut(25, 50, 100)
print(weasley)

#galleons = potter.galleons + weasley.galleons
#sickles = potter.sickles + weasley.sickles
#knuts = potter.knuts + weasley.knuts

# with operator overloading
# docs.python.org/3/reference/datamodel.html#special-method-names

# object.__add__(self, other)

total = Vault(galleons, sickles, knuts)
print(total)
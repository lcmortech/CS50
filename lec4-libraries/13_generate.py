import random
# from random import choice

coin = random.choice("heads", "tails")

print(coin)

#random.randint(a, b)
number = random.randint(1, 10)
print(number)

# random.shuffle(x)
# it shuffles the argument in place
cards = ["jack", "queen", "king"]
random.shuffle(cards)

for card in cards:
    print(card)
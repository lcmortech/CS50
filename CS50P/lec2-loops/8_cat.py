# Exploring Loops
'''
print("meow")
print("meow")
print("meow")
'''

# we can express a loop with the WHILE keyword
# WHILE is a construct that allows us to ask a question again and again, where the answer is a bool (True or False)

# give a variable and initialize it to 3

'''
i = 3

while i > 0:
    print("meow")
    i -= 1 
'''
'''
i = 1
while i <= 3:
    print("meow")
    i += 1
    '''
# decrement/increment necessary to prevent an infinite loop

# introducing the for loop and lists
# the for loop simplifies alot of the processes of a while lop

# more pythonic to add an underscore than i as a default iterator
'''
for _ in range(4):
    print("meow")
'''

# more pythonic overall, but a bit unreadable
print("meow \n" * 3,end="")

# when you want to get user input that matches a certain expectation you have, you use while True:
'''
n = int(input("What's n? "))
if n < 0:
    n = int(input)... # gets confusing
'''

# introducing continue and break statements
'''
while True:
    n = int(input("What's n? "))
    if n < 0:
        continue
    else:
        break
'''

# more useable and common 
# break has the effect of breaking out the most recently begun while loop

'''
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")
'''

def main():
    num = get_number()
    meow(num)

# getter function
def get_number:
    while True:
        n = int(input("What's n? "))
        if n > 0:
            # break
            return n
    #return n

def meow(n):
    for _ in range(n):
        print("meow")
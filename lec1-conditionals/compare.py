x = int(input("What is X? "))
y=int(input("What is Y?" ))

if x < y:
    print("x is less than y")
# adding elif(else if) helps make the code more readable and logical
elif x > y:
    print("x is greater than y")
elif x == y: # can be replaced with else
    print("x is equal to y")
    
# else is not necessary here because all conditions have already been satisfied
'''
if x < y or x > y:
    print("x is not equal to y")
else:
    print("x is equal to y")
'''

try:
    x = int(input("What's x? "))
    print(f"x is {x}")

except ValueError:
    print("Please input a number")

# problem with NameError (due to the order of operations)
else:
    print(f"x is {x}")
# the user might input a string (value error)
# it's good to be specific with the error instead of leaving "except" as is
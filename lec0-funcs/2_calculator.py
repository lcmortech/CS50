'''
x = input("What's x? ")
y = input("What's y? ")

z = x + y

print(z)
>>> 12
# Python treats the inputs as strings by default, so the ans is "1" + "2" = "12"
'''

# You can nest functions, so that the return value of the inner function, becomes the argument ofthe outermost function
x = int(input("What's x?" ))
y = int(input("What's y?" ))

z = x + y
# alt z = int(x) + int(y)

# >>> 3

# you can do floating point numbers (floats)
x = float(input("What is x? "))
y = float(input("What is y? "))


# if x = 1.2, and y = 3.4
# >>> 4.6

# if you want to round the floats
x = float(input("What is x? "))
y = float(input("What is y? "))

z = round(x + y)

# if you want to include commas
print(f"{z:,}")

# you can also round to number of digits
round(x / y, 2)
>>> 0.67

# the way to specify digits using fstrings
print(f"{z:.2f}")
>>> 0.67


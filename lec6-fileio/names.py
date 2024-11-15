# names = []

# # for _ in range(3):
# #     name = input("What's your name?" )
# #     names.append[name]
# # # print(f"hello, {name}")
# # v2
# for _ in range(3):
# 	names.append(input("What's your name?" ))

# for name in sorted(names):
# 	print(f"hello", {name})
# # made shorter

# OPEN keyword - allows you to specify what you want to read from or write to

# names = input("What's your name? ")

# file = open("names.txt", "w") # creates file and allows you to write to it
# file.write(f"{name}\n")
# file.close()

# by changing the "w" to "a", the file goes from rewritable to editable (append)

# instead of using file.close(), we can use the with keyword instead

names = input("What's your name? ")

with open("names.txt", "a") as file:
file.write(f"{name}\n")
# file.close()

# w, a, r (write, append/edit, read)

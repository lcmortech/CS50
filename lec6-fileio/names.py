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

names = input("What's your name? ")

file = open("names.txt", "w") # creates file and allows you to write to it
file.write(name)
file.close()
# Ask user for their name
name = input("What is your name?").strip().title()

# Split user's name into first name and last name
first, last = name.split("")

# Say hello to user
print(f"Hello, {first}")
# Revisiting hello.py

'''
# My way
def hello(name):
    #name = input("What is your name? ").strip().title()
    name.strip().title
    print(f"Hello, {name}")

hello("Ren")
'''

# David's Way
def hello(to="world"): #assigning the default value "world"
    print("hello",", to)

hello()
name = input("What is your name? ")
hello(name)

# convention
def main():
    name = input("What is your name? ")

def hello():
    print("hello,",to)

# invoke functions (scope)
main()
hello()

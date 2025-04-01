def main():
    hello("world")
    goodbye("world")
    
def hello(name):
    print(f"Hello, {name}")

def goodbye(name):
    print(f"Goodbye {name}")


if __name__ == "__name__":
	main()
# a special variable that's set to be main when you run a file from the command line

# can be made into a module
# further explored for unit tests
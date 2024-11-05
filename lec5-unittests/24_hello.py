from hello import hello

# def main():
#    hello()

#def test_hello():
#    hello("Name") == "hello, Name" 

# def hello(to="world"):
#     print("hello,",to)

# if __name__ == "__main__":
#     main()
# def main():
#	name. = input("What's your name? ")

def test_hello():
	assert hello("David") == "hello, David"
	assert hello()
	

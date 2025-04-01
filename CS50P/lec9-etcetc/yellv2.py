# map(function, iterable, ...)

def main():
    yell("This", "is", "CS50")

def yell(*words):
    #uppercased = map(str.upper, words) use str class, not parenthesis
    #using list comprehensions
    uppercased = [word.upper() for word in words] #its in brackets bc it returns a list. "list" comprehensions
    print(*uppercased)

if __name__ == "__main__":
    main()
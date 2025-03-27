# *args and **kwargs allows other functions to act like print

def main():
    #yell("This is CS50")
    #yell(["This", "is", "CS50"])
    yell("This", "is", "CS50")

#def yell(phrase):
#def yell(words):
def yell(*words):
    #print(phrase.upper())
    #for word in words:
    #    print(word, end="")
    uppercased = []
    for word in words:
        uppercased.append(word.upper())
    #print(uppercased) >> ["THIS", "IS", "CS50"]
    print(*uppercased) #>> THIS IS CS50

if __name__ == "__main__":
    main()
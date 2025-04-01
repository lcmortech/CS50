# generators
def main():
    n = int(input("What's n? "))
    #for i in range(n):
#       print("🐑" * i) # multiply = multidimensional?
        #print(sheep(i))
    for s in sheep(n):
        print(s)

#def sheep(n):
#    flock = []
#    for i in range(n):
#        flock.append("🐑" * i)
#    return flock  

# return - returns all the data at once
# yield - instead of return, just return one value at a time
# yield returns iterators which can be thought of as asynchrononous 

def sheep(n):
    for i in range(n):
        yield "🐑" * i


if __name__ == "__main__":
    main()

def main():
    name = get_name() # abstraction
    house = get_house()
    print(f"{name} from {house}")

def get_name():
        return input("Name: ")
    
def get_house():
        return input("House: ")

if__name__ == "__main__":
    main()


from calculator import square:

def main():
    test_square()

def test_square():
    #if square(2) != 4:
    #    print("2 squared was not 4")
    #if square(3) != 9:
    #    print("3 squared was not 9")

    try:
        assert square(2) == 4
    except AssertionError:
        print("2 squared was not 4")
    try:
        assert square(3) == 9
    except:
        print("3 squared was not 9")
	try:
        assert square(-2) == 4
    except AssertionError:
        print("-2 squared was not 4")
    try:
        assert square(-3) == 9
    except:
        print("-3 squared was not 9")
	try:
        assert square(0) == 0
    except AssertionError:
        print("0 squared was not 0")
if __name__ == "__main__":
    main()

# assert keyword - asserts that a boolean expression is true
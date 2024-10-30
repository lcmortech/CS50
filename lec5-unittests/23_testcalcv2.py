from 20_calculator import square

def test_square():
    assert square(2) == 4
    assert square(3) == 9
    assert square(-2) == 4
    assert square(-3) == 9
    assert square(0) == 0

# simply test using pytest, a third party tool
# pytest automates the testing process
# pytest only tests function given in test file, not all the logic in main
# it's better to break up your ideas into smaller bite-sized functions that are testable, like square(n)
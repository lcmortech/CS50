import pytest

from 20_calculator import square

#def test_square():
#    assert square(2) == 4
#    assert square(3) == 9
#    assert square(-2) == 4
#    assert square(-3) == 9
#    assert square(0) == 0

# vs

def test_positive():
	assert square(2) == 4
	assert square(3) == 9

def test_negative():
	assert square(-2) == 4
	assert square(-3) == 9

def test_zero():
	assert square(0) == 0	

def test_str():
	with pytest.raises(TypeError)
	square("cat")

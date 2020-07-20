import pytest
from programs import list_of_squares

def test_square():
    for i in range(1,21):
        assert list_of_squares.list_of_squares(i)[i]==i*i

def test_int():
    assert type(list_of_squares.list_of_squares(5)) is dict
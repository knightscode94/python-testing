import pytest
from programs import cotd23

def test_add():
    assert cotd23.addition(1)==1234
    assert cotd23.addition(9)==11106
import pytest
from programs import factorial

def test_fact():
    assert factorial.fact(0)==1

def test_xfact():
    assert factorial.fact(4)==24

def test_int():
    assert type(factorial.fact(5)) is int
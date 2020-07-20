import pytest
from programs import vowels
from string import ascii_letters
from random import choice


def test_vowels():
    assert vowels.vowels("aeiou")==5
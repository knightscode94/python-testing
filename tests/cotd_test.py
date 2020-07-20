
"""
I have a function called `string_gen()` that will return a random 5-character-long string of lowercase letters. Write some tests for this function.
To reiterate, the output should always be:
	
a string
5 characters long
comprised of lowercase letters
"""

import pytest
from programs import cotdtest

def test_str():
    assert type(cotdtest.string_gen()) is str


def test_len():
    assert len(cotdtest.string_gen())==5


def test_lower():
    assert (cotdtest.string_gen().islower())== True
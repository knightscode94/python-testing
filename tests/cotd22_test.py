import pytest
from programs import cotd22

def test_whitespace():
    assert cotd22.world("sunt in culpa qui officia deserunt mollit anim id est laborum") == "anim culpa deserunt est id in laborum mollit officia qui sunt"
    assert cotd22.world("a a a b b b b b b b b c c c c c") == "a b c"
    assert cotd22.world("cc ccc cc bb cc b a aaa b cc") == "a aaa b bb cc ccc"
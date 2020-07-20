"""
I have a function called `string_gen()` that will return a random 5-character-long string of lowercase letters. Write some tests for this function.
To reiterate, the output should always be:
	
a string
5 characters long
comprised of lowercase letters
"""
import random
import string


def string_gen():
    letters = string.ascii_lowercase
    result = "".join(random.choice(letters) for i in range(5))
    return result

print(string_gen())

print(string.ascii_lowercase)
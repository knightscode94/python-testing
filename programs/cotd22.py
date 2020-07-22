"""
Python Write a function that accepts a sequence of whitespace separated 
words as a string input, sorts each item alphanumerically and removes any duplicate items, 
then returns the result as a string.

 

Suppose the following input is supplied to the program: hello world and practice makes
perfect and hello world againThen, the output should be: again and hello makes perfect practice world

 
Hint: make use of the set() collection type!
"""

def world(input):
    output = " "
    input=input.split()
    input=set(input)
    input=sorted(input)
    return (output.join(input))

print(world("cc ccc cc bb cc b a aaa b cc"))
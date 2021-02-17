#Write a Python program to get the current value of the recursion limit.

#02_15_21

#Recursion is the process of defining something in terms of itself.

#A physical world example would be to place two parallel mirrors facing each other. 
#Any object in between them would be reflected recursively.

#sys.getrecursionlimit() method is used to find the current recursion limit 
#of the interpreter. This limit prevents any program from getting into infinite recursion.


import sys

print("Current value of the recursion limit:")
print(sys.getrecursionlimit())


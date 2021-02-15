#Write a Python program to get the details of math module.

#

import math

print(f"\n{math.__doc__}") #prints the docstring of the math module

math_details = dir(math) #dir - returns a list of valid attributes of an object
print("\nAll attributes of the math module:\n", ", ".join(math_details))
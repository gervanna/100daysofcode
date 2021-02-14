#Write a Python program to calculate the hypotenuse of a right angled triangle.

#02_13_21

import math

def find_hypotenuse(sidea, sideb):
    sidec = int(math.pow(sidea, 2) + math.pow(sideb, 2))
    print(f"The length of the hypotenuse is: {sidec}.")
    return sidec
find_hypotenuse(3, 4)
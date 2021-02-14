#Write a Python program to get the volume of a sphere with radius 6.

#02_11_21

import math

def volume_of_sphere(radius):
    '''Function that takes a radius and calculates the volume of a sphere'''
    #V = 4/3 πr³
    pi = math.pi
    radius_cube = math.pow(radius, 3)
    V = (4/3 * pi * radius_cube)
    result = round(V, 2)
    print(f"The volume of a sphere with radius {radius} is {result}.")
    return V
volume_of_sphere(6)
volume_of_sphere(float(input("Input a radius: ")))
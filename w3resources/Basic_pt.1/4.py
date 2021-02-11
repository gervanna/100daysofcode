#Write a Python program which accepts the radius of a circle from the user and compute the area.
#02_10_21

import math 

def calculate_circle_area(radius):
    '''Function that takes a radius and calculates the area of a circle'''
    pi = math.pi 
    radius_square = math.pow(radius, 2)
    area = pi * radius_square
    result = round(area, 2)
    print(f"The area of the circle is {result}.")
    return result
calculate_circle_area(3)
calculate_circle_area(float(input("Input a radius: ")))
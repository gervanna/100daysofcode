#Write a Python program to compute the 
#distance between the points (x1, y1) and (x2, y2).

#02_15_21

import math

def distBetweenPoints(point1, point2):
    # assuming point1 and point2 are a tuple or a list
    x1, y1 = point1
    x2, y2 = point2

    width_difference = x2 - x1
    height_difference = y2 - y1

    return math.sqrt(width_difference**2 + height_difference**2) 
    #this is pythagorus's theorem c^2 = a^2 + b^2

p1 = (4,5)
p2 = (7,9)

print("\nDistance between points\n", distBetweenPoints(p1, p2))

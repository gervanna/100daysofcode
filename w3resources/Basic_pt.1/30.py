#Write a Python program that will accept the 
#base and height of a triangle and compute the area.

#02_13_21

def area_triangle(base, height):
    result = base * height / 2
    print(f"The area of the triangle is {result}.")
    return result
area_triangle(5, 8)
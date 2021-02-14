#Write a Python program to convert height (in feet and inches) to centimeters.

#02_13_21

print("Enter your height in feet and inches. Enter only numbers.")
feet = int(input("Feet: "))
inches = int(input("Inches: "))

def convert_to_cm(feet, inches):
    feet_to_cm = feet * 30.48
    inches_to_cm = inches * 2.54
    centimeters = feet_to_cm + inches_to_cm
    print(f"Your height in centimeters is {centimeters}.")
    return centimeters
convert_to_cm(feet, inches)
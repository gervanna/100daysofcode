#Write a Python program to convert the distance (in feet) to inches, yards, and miles. 

#02_13_21

print("Enter the distance in feet. Only input the number.")

feet = int(input("Feet: "))

inches = feet * 12
yards = feet * 0.33333
miles = feet * 0.00018939

print(f"{feet}ft is {inches} in inches, {yards} in yards and {miles} in miles.")
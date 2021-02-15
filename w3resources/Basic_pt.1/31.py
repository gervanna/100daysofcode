#Write a Python program to compute the 
#greatest common divisor (GCD) of two positive integers. 

#02_15_21

def gcd(num1, num2):
    start = min(num1, num2) #uses min function to determine which num is smaller
    gcd = 1
    for n in range(start, 1, -1): #counting down from the largest possible value to one
        if (num1 % n == 0) and (num2 % n == 0): #check if n is a factor of both numbers
            gcd = n
            break
    return gcd #so a value will alwas be returned instead of none when there is no gcd

print("\nGCD\n", gcd(693, 1463))
print("\nGCD\n", gcd(12, 144))
print("\nGCD\n", gcd(5, 7))


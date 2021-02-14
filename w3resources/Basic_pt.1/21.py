#Write a Python program to find whether a given number (accept from the user)
#is even or odd, print out an appropriate message to the user.

#02_13_21

def odd_or_even(num):
    if num % 2 == 0:
        print(f"The number {num} is even.")
    else:
        print(f"The number {num} is odd.")
odd_or_even(int(input("Enter a number please: ")))
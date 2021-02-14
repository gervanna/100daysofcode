#Write a Python program to test whether a number is within 100 of 1000 or 2000.

#02_11_21

num1 = 1000
num2 = 2000

guess = (input("Type an integer: "))

try:
    guess_int = int(guess)
    if guess_int == 1000:
        print(f"The number you chose {guess_int} is exactly the number {num1}.")
    elif guess_int == 2000:
        print(f"The number you chose {guess_int} is exactly the number {num2}.")
    elif guess_int >= 900 and guess_int <= 1100:
        print(f"Your number is within 100 of the number {num1}.")
    elif guess_int >= 1900 and guess_int <= 2100:
        print(f"Your number is within 100 of the number {num2}.")
    else:
        print("Your number is way off.")
except:
    print("Bruv. No.")


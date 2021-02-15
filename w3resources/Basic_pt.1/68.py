#Write a Python program to calculate the sum of the digits in an integer.

#02_14_21

num = int(input("Enter a number: "))
sum_of_digits = sum(map(int, str(num)))

print(f"The sum of the digits of {num} is {sum_of_digits}.")
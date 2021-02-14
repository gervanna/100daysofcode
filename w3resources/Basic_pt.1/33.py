#Write a Python program to get the sum of three given integers. 
#However, if two values are equal sum will be zero.

#02_13_21

def total_or_zero(num1, num2, num3):
    sum = num1 + num2 + num3

    if num1 == num2 or num1 == num3 or num2 == num3:
        sum = 0
    return sum
print(total_or_zero(5, 8, 7)) #all nums diff.
print(total_or_zero(7, 12, 7)) #num1==num3
print(total_or_zero(10, 10, 8)) #num1==num2
print(total_or_zero(9, 10, 10)) #num2==num3
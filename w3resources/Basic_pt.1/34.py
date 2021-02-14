#Write a Python program to get the sum of two given integers. 
#However, if the sum is between 15 to 20 it will return 20.

#02_13_21

def sum_variation(num1, num2):
    sum = num1 + num2
    if sum in range(15, 20):
        sum = 20
    return sum
print(sum_variation(10, 6))
print(sum_variation(7, 7))
print(sum_variation(10, 11))
        
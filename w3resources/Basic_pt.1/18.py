#Write a Python program to calculate the sum of three given numbers, 
#if the values are equal then return three times of their sum.

#02_11_21

def sum_or_3times(num1, num2, num3):
    '''Takes 3 numbers and sums them. 
    If the numbers are all the same however, return 3 times the sum.'''
    
    sum = num1 + num2 + num3
    
    if num1 == num2 == num3:
        sum = sum * 3

    return sum
print("The sum is", sum_or_3times(4, 6, 12))
print("The sum multiplied by 3 is", sum_or_3times(3, 3, 3))
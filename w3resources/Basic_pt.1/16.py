#Write a Python program to get the difference between a given number and 17, 
#if the number is greater than 17 return double the absolute difference.

#02_14_21

def num_vs_17(num):
    if num == 17:
        result = 0
        print(f"Your result is {result}.")
        return result
    elif num < 17:
        result = 17 - num
        print(f"Your result is {result}.")
        return result
    elif num > 17:
        result = (num - 17) * 2
        print(f"Your result is {result}.")
        return result
num_vs_17(int(input("Type a number here: ")))
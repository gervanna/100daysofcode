#Write a python program to find the sum of the first n positive integers.

#02_13_21

def sum_1_to_n(num):
    result = int((num * (num + 1) / 2))
    print(f"The sum of the numbers 1 to {num} is {result}.")
    return result
sum_1_to_n(100)
sum_1_to_n(int(input("Type a number: ")))
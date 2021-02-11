#Write a Python program which accepts a sequence of comma-separated numbers 
#from user and generate a list and a tuple with those numbers.

#02_10_21

numbers = input("Enter a set a numbers and separate them by a comma: ")
num_list = numbers.split(",")
num_tuple = (tuple(num_list))
print(f"\nThis is a list: {num_list}")
print(f"\nThis is a tuple: {num_tuple}")
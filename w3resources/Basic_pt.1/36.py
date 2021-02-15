#Write a Python program to add two objects if both objects are an integer type.

#02_13_21

def same_type_add(value1, value2):
    sum = value1 + value2
    return sum

num1 = input("Enter a digit: ")
num2 = input("Enter another digit: ")

try:
    num_int1 = int(num1)
    num_int2 = int(num2)
    if type(num_int1) == int and type(num_int2) == int:
        print(same_type_add(num_int1, num_int2))
except:
    print("Next time type a integer bruv.")
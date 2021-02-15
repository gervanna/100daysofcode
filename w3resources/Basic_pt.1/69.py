#Write a Python program to sort three integers without using conditional statements and loops.

#02_14_21

def int_sort(str):
    num_list = str.split(",")
    numbers = map(int, num_list)
    sorted_nums = sorted(numbers)
    print(f"Numbers in sorted order: {sorted_nums}.")
    return sorted_nums

int_sort(input("Enter 3 numbers separated by commas: "))
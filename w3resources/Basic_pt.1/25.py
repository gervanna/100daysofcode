#Write a Python program to check whether a specified value is contained in a group of values.

#02_13_21

test1 = [4, 5, 8, 6, 2, 4, 8, 0]
test2 = [0, 8, 6, 2]
test3 = [4, 6, 4, 6 ,4, 9, 77, 44, 4]

def am_I_innit(data, num):
    if num in data:
        return True
    else:
        return False
print(am_I_innit(test1, 6))
print(am_I_innit(test2, -3))
print(am_I_innit(test3, 77))
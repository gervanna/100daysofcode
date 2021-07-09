#Write a Python program to test whether all numbers of a list is greater than a certain number.

#02_19_21

test = [6, 8, 9, 12]
test1 = [10, 99, 78]


def greater_checker(items, num):
    for i in items:
        if i > num:
            return True
        else:
            return False
print(greater_checker(test, 12))
print(greater_checker(test1, 5))
#Write a Python program to count the number 4 in a given list.

#02_13_21

test1 = [4, 5, 8, 6, 2, 4, 8, 0]
test2 = [0, 8, 6, 2]
test3 = [4, 6, 4, 6 ,4, 9, 77, 44, 4]

def four_count(lst):
    count_4 = lst.count(4)
    return count_4

print("The number of 4's is: ",(four_count(test1)))
print("The number of 4's is: ",(four_count(test2)))
print("The number of 4's is: ",(four_count(test3)))

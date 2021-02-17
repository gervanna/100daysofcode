#Write a Python program to swap two variables.

#02_16_21

test1 = 45
test2 = 20
print(f"\nOriginal variable assignment: {test1 = } and {test2 = }.")


test1, test2 = test2, test1
#variables swapped using multiple asignment
#swap could've also been done using a third temporary varible "test3"

print(f"\nSwapped variable assignment: {test1 = } and {test2 = }.")

#Write a Python program to get a new string from a given string 
#where "Is" has been added to the front. 
#If the given string already begins with "Is" then return the string unchanged.

#02_14_21

test_str = input("Type some words here: ")

if test_str[0:2] == "is" or test_str[0:2] == "Is":
    print(test_str)
else:
    print("Is " + test_str)

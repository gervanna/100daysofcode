#Write a Python program to get a string which is n 
#(non-negative integer) copies of a given string.

#02_14_21

def str_multiplier(str, num):
    result = (str)*num
    print(f"Your new string is {result}")
    return result
str_multiplier("Kirk", 5)
str_multiplier(".py", 10)
str_multiplier("Ha", 0)
